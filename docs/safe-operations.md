# Safe Operations

## Sensor containment

- Place honeypots on a dedicated network or isolated VPS.
- Block unsolicited sensor egress and test the block from the sensor namespace.
- Run containers without privilege escalation, unnecessary capabilities, or a
  writable root filesystem whenever the software permits it.
- Apply memory and process limits so hostile traffic cannot exhaust the host.
- Keep dashboards and administrative services private.

## Capture safety

- Never execute a captured artifact on the sensor or operator workstation.
- Keep captured files outside cloud-synchronized folders and source-control
  repositories.
- Use storage mounted with `nodev`, `nosuid`, and `noexec` where practical.
- Keep sample handling and malware analysis outside the scope of this public
  repository except for the high-level, manually controlled submission workflow
  described below.

## External services

- Review source-IP evidence before manually reporting abusive activity to
  AbuseIPDB.
- Remove operator test traffic and internal addresses from every report.
- Submit only deliberately selected captures to VirusTotal, ANY.RUN, or Hybrid
  Analysis; never automate unknown-file uploads.
- Keep service credentials, local storage paths, submitted files, and raw
  reports outside this public repository.

## Publication

- Publish aggregate findings or deliberately reviewed indicators only.
- Defang attacker-controlled URLs.
- Remove credentials, session transcripts, private keys, notification topics,
  hostnames, internal paths, and live network details.
- Never make an operational private repository public; publish from a separate,
  sanitized repository.
