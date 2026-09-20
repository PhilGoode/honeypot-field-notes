# Read-only Reporting Tools

These scripts summarize existing sensor data. They do not execute or upload
captured artifacts and do not modify sensor databases or logs.

The scripts in this directory are independently written reporting helpers for
data produced by the upstream projects credited in
[ACKNOWLEDGMENTS.md](../ACKNOWLEDGMENTS.md). No upstream source code is bundled
here.

## Cowrie

```bash
python3 cowrie_recent_transfers.py \
  --log-dir /path/to/cowrie/logs \
  --hours 24 --limit 50
```

## Dionaea

```bash
python3 dionaea_recent_captures.py \
  --database /path/to/dionaea.sqlite \
  --captures /path/to/binaries \
  --hours 24 --limit 50
```

## H0neytr4p

```bash
python3 h0neytr4p_recent_requests.py \
  --log /path/to/log.json \
  --hours 24 --port all --limit 50
```

Copying raw samples is outside the scope of these tools.
