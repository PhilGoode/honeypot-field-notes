# Sanitized Research Highlights

For the detailed narratives, see [Sanitized Case Studies](case-studies.md). For
the aggregate counts and definitions, see [Measurement Snapshot](metrics.md).

## SMB delivery campaigns

An exposed SMB emulator received repeated deliveries of closely related Windows
payloads. Repeated transfers and recurring source behavior showed why event
counts, unique sources, and unique stored objects should be reported as
separate measurements. Three reviewed result sets contained 75 distinct
SHA-256 values, most associated publicly with WannaCry-family activity.

## SSH and Telnet payload diversity

Interactive-service telemetry captured shell scripts and Linux executables for
multiple processor architectures. The architecture spread is consistent with
commodity campaigns attempting to infect routers, embedded systems, and cloud
hosts from one deployment chain. This public summary does not include the
captured files. One delivery set alone covered ARM, AArch64, x86, x86-64, and
RISC-V.

## HTTP exploitation traffic

Web sensors observed high-volume requests for exposed environment files,
version-control metadata, framework debugging endpoints, vulnerable dependency
paths, container APIs, and common web-shell locations. A small number of source
addresses generated most requests, demonstrating why request counts alone are
not equivalent to unique attackers.

Across the published snapshots, the web sensors recorded 27,935 request events
and 845 trap matches. All recorded payload events in those snapshots were
controlled validation tests and were excluded from attacker findings.

## Operational lessons

- Reusable reporting scripts prevent inconsistent one-off queries.
- Capture notifications should fire only after the sensor records a completed
  event.
- Source-plus-event deduplication reduces alert fatigue without hiding repeated
  activity from a new source.
- Public findings are most useful when they explain methodology and limitations
  rather than presenting unsanitized telemetry dumps.
