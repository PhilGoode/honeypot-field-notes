#!/usr/bin/env python3
"""Summarize recent Cowrie transfer events without modifying evidence."""

from __future__ import annotations

import argparse
import gzip
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path


EVENTS = {
    "cowrie.session.file_upload": "upload",
    "cowrie.session.file_download": "download",
    "cowrie.session.file_download.failed": "failed-download",
}
IP_RE = re.compile(r"(?<![\d.])(\d{1,3}(?:\.\d{1,3}){3})(?![\d.])")


def parse_time(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def safe(value: object) -> str:
    text = str(value or "-").replace("\r", " ").replace("\n", " ")
    text = text.replace("https://", "hxxps://").replace("http://", "hxxp://")
    return IP_RE.sub(lambda match: match.group(1).replace(".", "[.]"), text)


def events(path: Path):
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", errors="replace") as stream:
        for line in stream:
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                yield value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log-dir", type=Path, required=True)
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()
    if not 1 <= args.hours <= 168 or not 1 <= args.limit <= 500:
        parser.error("--hours must be 1-168 and --limit must be 1-500")
    if not args.log_dir.is_dir():
        parser.error(f"log directory not found: {args.log_dir}")

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    records: dict[tuple[str, str, str, str], dict] = {}
    event_count = 0
    for path in sorted(args.log_dir.glob("cowrie.json*")):
        for event in events(path):
            kind = EVENTS.get(str(event.get("eventid")))
            moment = parse_time(event.get("timestamp"))
            if not kind or moment is None or moment < cutoff:
                continue
            event_count += 1
            source = str(event.get("src_ip") or "-")
            digest = str(event.get("sha256") or event.get("shasum") or "-")
            name = str(event.get("filename") or event.get("url") or "-")
            key = (source, kind, digest, name)
            record = records.setdefault(
                key,
                {"time": moment, "source": source, "kind": kind, "hash": digest,
                 "name": name, "protocol": event.get("protocol") or "-", "count": 0},
            )
            record["count"] += 1
            record["time"] = max(record["time"], moment)

    print("UTC time | source | protocol | transfer | name or URL | SHA-256 | events")
    for record in sorted(records.values(), key=lambda item: item["time"], reverse=True)[: args.limit]:
        print(
            f"{record['time'].isoformat()} | {safe(record['source'])} | "
            f"{safe(record['protocol'])} | {record['kind']} | {safe(record['name'])} | "
            f"{record['hash']} | {record['count']}"
        )
    print(f"\nTransfer events: {event_count}")
    print(f"Unique rows: {len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
