# Reference Architecture

The design separates collection, management, reporting, and analysis so a
compromised sensor cannot become a convenient path into the operator's normal
network.

```text
Internet
   |
   v
[Provider or edge firewall]
   |
   v
[Isolated honeypot network]
   |-- Cowrie: SSH and Telnet interaction
   |-- Dionaea: SMB and selected service emulation
   `-- H0neytr4p: HTTP and HTTPS request collection
   |
   +--> append-only logs and bounded capture storage
   +--> metadata-only notifications
   `--> default-deny outbound policy

Separate management path
   |
   +--> authenticated administration
   +--> read-only reporting tools
   `--> manually reviewed external reporting or sandbox submission
```

## Design principles

1. Treat every sensor as disposable and untrusted.
2. Keep administration off public honeypot ports.
3. Deny new outbound connections from capture containers by default.
4. Persist logs and captures outside ephemeral container layers.
5. Send metadata in notifications, never payload attachments.
6. Summarize events using timestamps, protocol metadata, and source data.

This layout is intentionally generic. It does not disclose a live deployment's
addresses, credentials, notification channels, or provider configuration.
