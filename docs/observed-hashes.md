# Selected Observed Hashes

The SHA-256 indicators below represent distinctive files captured by the
Cowrie and Dionaea sensors. This is a curated research list, not a complete
inventory of every capture. Repetitive variants and trivial text artifacts are
omitted.

Family labels reflect public scanner classifications recorded when the hashes
were reviewed. They can change as vendors update their detections and should
not be treated as independent attribution by this project. Links perform
hash-only VirusTotal lookups; no samples are stored in this repository.

## Cowrie SSH and Telnet captures

| SHA-256 | Observed type | Public classification at review |
|---|---|---|
| [`7b1cbba56bb80e185cdf2097f5716c31d7e0f88f28ad7220b3b5a2cf73859ec8`](https://www.virustotal.com/gui/file/7b1cbba56bb80e185cdf2097f5716c31d7e0f88f28ad7220b3b5a2cf73859ec8) | Shell script | Downloader |
| [`73695282607747038a31f516e3f8310a67ae6f2f9e4a0b90b55a40f77272e559`](https://www.virustotal.com/gui/file/73695282607747038a31f516e3f8310a67ae6f2f9e4a0b90b55a40f77272e559) | Linux ELF | Gafgyt/Mirai |
| [`cd9655a77201f73e69953ec5b53f898de41983c1b4dcedd0c431955b9c20b241`](https://www.virustotal.com/gui/file/cd9655a77201f73e69953ec5b53f898de41983c1b4dcedd0c431955b9c20b241) | Linux ELF | Gafgyt/Mirai |
| [`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656`](https://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656) | Linux ELF | Gafgyt/Tsunami |
| [`3f3a11bafabb1a35db913cfe51995f2e357d049e268860175876ae5a93d23892`](https://www.virustotal.com/gui/file/3f3a11bafabb1a35db913cfe51995f2e357d049e268860175876ae5a93d23892) | Shell script | Qwexlafiba/RedTail-associated script |
| [`d70f917e35813a7ae323e6b2b539d6dbbfc3a3a6599f1fed93430b14ca08b141`](https://www.virustotal.com/gui/file/d70f917e35813a7ae323e6b2b539d6dbbfc3a3a6599f1fed93430b14ca08b141) | ARM ELF | Miner/ABMiner |
| [`d1cac82f44b54b0fd244a9e4122811e9ae108a197c7a65a20fd2e7552683e68e`](https://www.virustotal.com/gui/file/d1cac82f44b54b0fd244a9e4122811e9ae108a197c7a65a20fd2e7552683e68e) | AArch64 ELF | MalXMR |
| [`8e1a67a5c03b3cd818f046c7a1605afccc0ee5ce437a0d099881f1872b54bc70`](https://www.virustotal.com/gui/file/8e1a67a5c03b3cd818f046c7a1605afccc0ee5ce437a0d099881f1872b54bc70) | x86 ELF | MalXMR |
| [`3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39`](https://www.virustotal.com/gui/file/3f3bf218089d1488617d37f8a5116bb2791eb39ce06a1b5bc9a4cdfe5e94dd39) | RISC-V ELF | Multiverze |
| [`f0aa83bbbd2c75e2f71ec16029ee5fcfad59f3a8efa30a500b815f0f6c18d987`](https://www.virustotal.com/gui/file/f0aa83bbbd2c75e2f71ec16029ee5fcfad59f3a8efa30a500b815f0f6c18d987) | x86-64 ELF | MalXMR |
| [`1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d`](https://www.virustotal.com/gui/file/1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d) | Shell script | SAgent |

## Dionaea SMB captures

| SHA-256 | Observed type | Public classification at review |
|---|---|---|
| [`815eccf206bc39d67ad9c903c823cc76c59ebb5e0e24ff1028b5242c53686a3a`](https://www.virustotal.com/gui/file/815eccf206bc39d67ad9c903c823cc76c59ebb5e0e24ff1028b5242c53686a3a) | Windows PE DLL | Midie/ZombieBoy |
| [`365bd32183bea8c84c6d047e5cc037e100b4a1a724ffc3c7f78a67806f030f59`](https://www.virustotal.com/gui/file/365bd32183bea8c84c6d047e5cc037e100b4a1a724ffc3c7f78a67806f030f59) | Windows PE DLL | WannaCry/WannaCrypt behavior; first submitted to VirusTotal by this project |

## Use and handling

These indicators are published for defensive correlation and research. A hash
alone does not prove that a file is malicious, establish attribution, or show
that two differently hashed files behave identically. Do not retrieve or
execute a corresponding sample outside an appropriately isolated and authorized
analysis environment.
