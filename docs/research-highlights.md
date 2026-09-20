# Sanitized Research Highlights

## SMB delivery campaigns

An exposed SMB emulator received repeated deliveries of closely related Windows
payloads. Repeated transfers and recurring source behavior showed why event
counts, unique sources, and unique stored objects should be reported as
separate measurements.

## SSH and Telnet payload diversity

Interactive-service telemetry captured shell scripts and Linux executables for
multiple processor architectures. The architecture spread is consistent with
commodity campaigns attempting to infect routers, embedded systems, and cloud
hosts from one deployment chain. This public summary does not include the
captured files or their analysis.

## HTTP exploitation traffic

Web sensors observed high-volume requests for exposed environment files,
version-control metadata, framework debugging endpoints, vulnerable dependency
paths, container APIs, and common web-shell locations. A small number of source
addresses generated most requests, demonstrating why request counts alone are
not equivalent to unique attackers.

## Operational lessons

- Reusable reporting scripts prevent inconsistent one-off queries.
- Capture notifications should fire only after the sensor records a completed
  event.
- Source-plus-event deduplication reduces alert fatigue without hiding repeated
  activity from a new source.
- Public findings are most useful when they explain methodology and limitations
  rather than presenting unsanitized telemetry dumps.
