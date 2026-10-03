# Sanitized Research Highlights

For the detailed narratives, see [Sanitized Case Studies](case-studies.md). For
the aggregate counts and definitions, see [Measurement Snapshot](metrics.md).

## SMB delivery campaigns

An exposed SMB emulator received repeated deliveries of closely related Windows
payloads. Repeated transfers and recurring source behavior showed why event
counts, unique sources, and unique stored objects should be reported as
separate measurements. Four reviewed result sets contained 118 distinct
SHA-256 values, most associated publicly with WannaCry-family activity. In the
newest 43-hash set, two hashes had no VirusTotal record at lookup time; manual
submission later identified one as another WannaCry-family variant.

## SSH and Telnet payload diversity

Interactive-service telemetry captured shell scripts and Linux executables for
multiple processor architectures. The architecture spread is consistent with
commodity campaigns attempting to infect routers, embedded systems, and cloud
hosts from one deployment chain. This public summary does not include the
captured files. One delivery set alone covered ARM, AArch64, x86, x86-64, and
RISC-V.

The collection now combines a contained VPS deployment with a dedicated T-Pot
host on a separate sensor network. Cowrie and selected malware-capture traffic
use narrowly scoped, fail-closed VPN egress rather than a whole-host tunnel.
Captured files persist on separately mounted `noexec` storage, while
administration remains private.

## HTTP exploitation traffic

Web sensors observed high-volume requests for exposed environment files,
version-control metadata, framework debugging endpoints, vulnerable dependency
paths, container APIs, and common web-shell locations. A small number of source
addresses generated most requests, demonstrating why request counts alone are
not equivalent to unique attackers.

Across the published snapshots, the web sensors recorded 27,935 request events
and 845 trap matches. All recorded payload events in those snapshots were
controlled validation tests and were excluded from attacker findings.

Specialized collectors now add narrow views of NetScaler exploitation,
Android Debug Bridge exposure, and Log4Shell-style lookup payloads. The ADB and
Log4Shell collectors can retrieve observed HTTP/S payload URLs only through a
VPN-routed, fail-closed path. Retrieval targets in private, reserved, metadata,
or non-VPN address space remain blocked, and captured content lands on bounded
`noexec` storage.

## First live-malware set from T-Pot

The dedicated T-Pot host produced its first retained live-malware set after the
capture disk and isolation controls were accepted. Hash-only reputation lookup
associated the selected files with known Medusa downloader, Mirai, and
Multiverze activity. This was new to this collection, not a claim of newly
discovered malware. The public record therefore preserves family-level context
without publishing raw files or treating every transfer as unique content.

## Unified collection and visualization

Metadata collection now runs as a single census per collection plane. Each
census generates deterministic hashes and a sanitized analysis subset, which
reduces inconsistent one-off queries while keeping raw evidence out of the
handoff. Private dashboards provide an all-sensor view, capture hashes, and
source activity; an animated map is paced and visually deduplicated so a burst
from one source does not obscure unrelated events. Raw totals remain available
for analysis.

## Operational lessons

- Reusable reporting scripts prevent inconsistent one-off queries.
- Capture notifications should fire only after the sensor records a completed
  event.
- Source-plus-event deduplication reduces alert fatigue without hiding repeated
  activity from a new source.
- Low-value protocol connection alerts are more useful as hourly summaries
  grouped by protocol and source; completed-file captures still justify
  immediate metadata-only notification.
- Research tooling should not share a sensor's identity or route. SpiderFoot
  enrichment therefore uses a separate VPN path and remains constrained to
  passive intelligence and explicitly authorized targets.
- Public findings are most useful when they explain methodology and limitations
  rather than presenting unsanitized telemetry dumps.
- Dashboard convenience must not collapse evidence states: observed,
  captured, archived, hash-looked-up, analyzed, and publicly reported are
  tracked separately.
