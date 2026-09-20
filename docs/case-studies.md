# Sanitized Case Studies

These case studies preserve useful technical findings while withholding source
addresses, credentials, private infrastructure details, and raw samples.

## 1. ZombieBoy appears in the SMB collection

Dionaea captured an 82,435-byte Windows PE DLL with SHA-256:

[`815eccf206bc39d67ad9c903c823cc76c59ebb5e0e24ff1028b5242c53686a3a`](https://www.virustotal.com/gui/file/815eccf206bc39d67ad9c903c823cc76c59ebb5e0e24ff1028b5242c53686a3a)

At review time, VirusTotal reported 61 malicious detections out of 74 engines
and labeled it `trojan.midie/zombieboy`. Hybrid Analysis scored the sample
100/100 and identified `Midie.Generic` behavior. The sandbox record included a
ZombieBoy YARA match, execution through `regsvr32.exe`, local-network discovery,
API hooking, and communication logic for a remote endpoint.

This was the first ZombieBoy-family specimen in this collection, but not a
first-ever discovery: the exact hash had already appeared in public sandbox
records in 2020. That distinction matters. “New to this sensor” is not the same
as “new malware.”

## 2. A first VirusTotal submission, but not a zero-day

Another Dionaea delivery produced a 5,267,459-byte Windows DLL with SHA-256:

[`365bd32183bea8c84c6d047e5cc037e100b4a1a724ffc3c7f78a67806f030f59`](https://www.virustotal.com/gui/file/365bd32183bea8c84c6d047e5cc037e100b4a1a724ffc3c7f78a67806f030f59)

The initial hash-only VirusTotal lookup returned `not_found`, and this project
then made the first VirusTotal submission of that exact hash. A later Hybrid
Analysis run scored it 100/100 and associated its behavior with the known
WannaCry/WannaCrypt ecosystem and MS17-010-era SMB activity.

The finding was initially exciting enough to invite the phrase “zero-day,” but
the evidence did not support that claim. A previously unindexed specimen hash
can still be a variant of well-known malware using old techniques. Microsoft
published [MS17-010](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)
in March 2017. The sandbox report referenced CVE-2017-0147; Microsoft classifies
that specific CVE as an SMBv1 information-disclosure vulnerability within the
larger bulletin. The careful conclusion is therefore **first submission of this
hash**, not discovery of a new vulnerability.

## 3. One Cowrie session delivers a five-architecture toolset

A Cowrie session attempted to install an attacker-controlled SSH public key and
delivered two shell scripts plus statically linked Linux executables for ARM,
AArch64, x86, x86-64, and RISC-V.

Public scanner classifications included MalXMR, ABMiner, Multiverze, and
shell-based downloader families. The mix demonstrates a common commodity
strategy: deliver a small dispatcher script, determine the victim's CPU
architecture, and launch the matching binary. The attacker does not need to
know the target architecture before connecting.

The sensor did not execute the real binaries. Cowrie recorded the interaction
and retained the transferred content for isolated review.

## 4. Web probes reveal automation, not careful targeting

The HTTP and HTTPS sensors recorded 27,935 request events across two snapshots.
Common targets included:

- `.env` variants and exposed application configuration;
- `.git/config`, `.git/HEAD`, and CI workflow metadata;
- PHPUnit `eval-stdin.php` paths across many guessed directories;
- ThinkPHP function-invocation routes;
- PHP `pearcmd` path manipulation;
- Docker's unauthenticated `/containers/json` endpoint; and
- common administrative panels and web-shell locations.

The requests marched through long path lists with minimal delay and were highly
concentrated among a few sources. This looked like broad vulnerability scanning,
not a human operator carefully studying one application. It also illustrates
why “requests received” and “attackers observed” are different metrics.

## Cross-cutting lessons

1. Preserve exact hashes and timestamps, but do not overstate what they prove.
2. Separate event counts, unique sources, transfers, and unique content.
3. Treat vendor family labels as evolving enrichment, not ground truth.
4. Exclude validation traffic before drawing conclusions.
5. Keep public findings reproducible without publishing the raw evidence.
