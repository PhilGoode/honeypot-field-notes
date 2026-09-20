#!/usr/bin/env python3
"""Summarize recent public H0neytr4p HTTP and HTTPS request metadata."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path


IP_RE = re.compile(r"(?<![\d.])(\d{1,3}(?:\.\d{1,3}){3})(?![\d.])")


def parse_time(value: object) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def public_ip(value: object) -> bool:
    try:
        return ipaddress.ip_address(str(value)).is_global
    except ValueError:
        return False


def safe(value: object) -> str:
    text = str(value or "-").replace("\r", " ").replace("\n", " ")
    text = text.replace("https://", "hxxps://").replace("http://", "hxxp://")
    return IP_RE.sub(lambda match: match.group(1).replace(".", "[.]"), text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--port", choices=("80", "443", "all"), default="all")
    args = parser.parse_args()
    if not 1 <= args.hours <= 168 or not 1 <= args.limit <= 500:
        parser.error("--hours must be 1-168 and --limit must be 1-500")
    if not args.log.is_file():
        parser.error(f"log not found: {args.log}")

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    records: list[dict] = []
    sources: Counter[str] = Counter()
    payloads = trapped = 0
    with args.log.open(encoding="utf-8", errors="replace") as stream:
        for line in stream:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            moment = parse_time(event.get("timestamp"))
            source = str(event.get("src_ip") or "")
            port = str(event.get("dest_port") or "")
            if moment is None or moment < cutoff or not public_ip(source):
                continue
            if args.port != "all" and port != args.port:
                continue
            records.append(event)
            sources[source] += 1
            payloads += int(bool(event.get("payload_filename")))
            trapped += int(str(event.get("trapped", "")).lower() == "true")

    print(f"Public requests: {len(records)}")
    print(f"Unique public sources: {len(sources)}")
    print(f"Payload captures: {payloads}")
    print(f"Trapped requests: {trapped}\n")
    print("Top sources:")
    for source, count in sources.most_common(20):
        print(f"{count:6d}  {safe(source)}")
    print("\nLatest events:")
    for event in records[-args.limit :]:
        print(
            f"{safe(event.get('timestamp'))} | port={safe(event.get('dest_port'))} | "
            f"{safe(event.get('src_ip'))} | {safe(event.get('request_method'))} | "
            f"{safe(event.get('request_uri'))} | payload={bool(event.get('payload_filename'))} | "
            f"trapped={str(event.get('trapped', '')).lower() == 'true'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
