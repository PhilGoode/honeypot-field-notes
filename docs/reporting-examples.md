# Reporting Examples

The examples below use reserved documentation addresses and synthetic hashes.
They demonstrate output shape only; they are not real incident records.

## Cowrie transfer summary

```text
UTC time | source | protocol | transfer | name or URL | SHA-256 | events
2026-09-20T12:14:08+00:00 | 203[.]0[.]113[.]24 | ssh | download | hxxp://198[.]51[.]100[.]8/payload | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa | 1

Transfer events: 1
Unique rows: 1
```

The tool groups identical source/type/hash/name combinations while preserving
the newest timestamp and total event count.

## Dionaea capture summary

```text
UTC time | source | protocol | stored ID | SHA-256 | bytes | URL
2026-09-20T12:18:31+00:00 | 198[.]51[.]100[.]44 | smb | 0123456789abcdef0123456789abcdef | bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb | 5267459 | smb://-

Capture events shown: 1
```

The SQLite database is opened read-only. SHA-256 is calculated from the stored
capture without executing or modifying it.

## H0neytr4p request summary

```text
Public requests: 42
Unique public sources: 7
Payload captures: 0
Trapped requests: 5

Top sources:
    18  192[.]0[.]2[.]40

Latest events:
2026-09-20T12:20:00Z | port=443 | 192[.]0[.]2[.]40 | GET | /.env | payload=False | trapped=True
```

Only globally routable source addresses from the real input are counted. Output
replaces dots in IP addresses with `[.]` and changes `http`/`https` URLs to
`hxxp`/`hxxps` so reports are safer to share.

## Why publish the examples?

The examples make the scripts understandable without shipping private logs or
forcing readers to operate a honeypot. They also document the safety properties
that should remain stable if the tools evolve.
