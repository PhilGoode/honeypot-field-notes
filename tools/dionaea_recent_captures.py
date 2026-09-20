#!/usr/bin/env python3
"""Summarize recent Dionaea downloads using a read-only SQLite connection."""

from __future__ import annotations

import argparse
import hashlib
import re
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path


IP_RE = re.compile(r"(?<![\d.])(\d{1,3}(?:\.\d{1,3}){3})(?![\d.])")


def safe(value: object) -> str:
    text = str(value or "-").replace("\r", " ").replace("\n", " ")
    text = text.replace("https://", "hxxps://").replace("http://", "hxxp://")
    return IP_RE.sub(lambda match: match.group(1).replace(".", "[.]"), text)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--captures", type=Path, required=True)
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()
    if not 1 <= args.hours <= 168 or not 1 <= args.limit <= 500:
        parser.error("--hours must be 1-168 and --limit must be 1-500")
    if not args.database.is_file() or not args.captures.is_dir():
        parser.error("database or capture directory not found")

    cutoff = (datetime.now(timezone.utc) - timedelta(hours=args.hours)).timestamp()
    database = sqlite3.connect(f"file:{args.database}?mode=ro", uri=True)
    try:
        rows = database.execute(
            """
            SELECT c.connection_timestamp, c.remote_host, c.connection_protocol,
                   d.download_md5_hash, d.download_url
            FROM downloads AS d JOIN connections AS c
              ON c.connection = d.connection
            WHERE c.connection_timestamp >= ?
            ORDER BY c.connection_timestamp DESC LIMIT ?
            """,
            (cutoff, args.limit),
        ).fetchall()
    finally:
        database.close()

    print("UTC time | source | protocol | stored ID | SHA-256 | bytes | URL")
    for stamp, source, protocol, stored_id, url in rows:
        artifact = args.captures / str(stored_id or "")
        digest = sha256(artifact) if artifact.is_file() else "-"
        size = artifact.stat().st_size if artifact.is_file() else 0
        moment = datetime.fromtimestamp(float(stamp), timezone.utc).isoformat()
        print(
            f"{moment} | {safe(source)} | {safe(protocol)} | {stored_id or '-'} | "
            f"{digest} | {size} | {safe(url)}"
        )
    print(f"\nCapture events shown: {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
