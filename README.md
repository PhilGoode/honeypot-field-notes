# Honeypot Field Notes

Practical, defensive notes from operating isolated internet-facing honeypots.
This repository focuses on repeatable sensor operations, containment, metadata
reporting, and lessons learned from real unsolicited traffic.

## What this repository contains

- A vendor-neutral reference architecture for isolated honeypot sensors.
- Read-only reporting tools for Cowrie, Dionaea, and H0neytr4p logs.
- Operational safety practices for running exposed sensors.
- Sanitized research highlights from SSH, Telnet, SMB, HTTP, and HTTPS traffic.
- A curated list of distinctive SHA-256 indicators observed by the sensors.
- Design notes for notification and event deduplication.

## What this repository intentionally excludes

- Raw malware or captured payloads.
- Credentials, tokens, notification topics, SSH details, or internal paths.
- Public or private sensor addresses and network topology.
- Raw attacker sessions, unsanitized logs, or bulk-reporting files.
- Raw sandbox reports, sample collections, or removable-media workflows.
- Exploit deployment, persistence, command-and-control, or offensive automation.

## Project layout

```text
.
├── ACKNOWLEDGMENTS.md
├── README.md
├── SECURITY.md
├── docs/
│   ├── architecture.md
│   ├── observed-hashes.md
│   ├── research-highlights.md
│   └── safe-operations.md
└── tools/
    ├── README.md
    ├── cowrie_recent_transfers.py
    ├── dionaea_recent_captures.py
    └── h0neytr4p_recent_requests.py
```

## Defensive scope

These materials are intended for systems you own or are authorized to operate.
The reporting tools read existing logs and metadata; they do not execute
payloads, exploit systems, upload samples, or report addresses automatically.

## External reporting and sandboxing

After manual review, supported workflows may report well-evidenced abusive
source addresses to [AbuseIPDB](https://www.abuseipdb.com/) and submit selected
captures to [VirusTotal](https://www.virustotal.com/),
[ANY.RUN](https://app.any.run/), or
[Hybrid Analysis](https://www.hybrid-analysis.com/). Those actions remain
operator-controlled. This repository does not contain credentials, API keys,
captured files, private storage paths, or raw sandbox reports.

## Upstream projects

This work builds on the open-source honeypot community, particularly T-Pot,
Cowrie, Dionaea, and H0neytr4p. See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for
official project links, attribution, and the relationship of each project to
these field notes.

## Status

This is a public working repository. Its contents will evolve as additional
material is reviewed and sanitized for release. No open-source license has been
selected yet; publication alone does not grant permission to reuse the code or
documentation.
