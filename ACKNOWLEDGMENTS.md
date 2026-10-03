# Acknowledgments

This repository documents independent defensive research and includes original
read-only reporting helpers. It does not create, maintain, or redistribute the
honeypot projects listed below. The work is possible because their maintainers
make these tools available to the security community.

## Upstream projects

- [T-Pot](https://github.com/telekom-security/tpotce), maintained by Deutsche
  Telekom Security GmbH, provides a multi-honeypot platform and informs the
  isolated sensor architecture discussed in these field notes.
- [Cowrie](https://github.com/cowrie/cowrie) provides the SSH and Telnet
  honeypot whose event and file-transfer records are summarized by the Cowrie
  reporting helper.
- [Dionaea](https://github.com/DinoTools/dionaea) provides malware-capture and
  service-emulation capabilities, including the SMB observations discussed in
  this repository.
- [H0neytr4p](https://github.com/pbssubhash/h0neytr4p), originally developed by
  its upstream maintainers and also distributed through the
  [T-Pot H0neytr4p package](https://github.com/telekom-security/tpotce/pkgs/container/h0neytr4p),
  provides the HTTP and HTTPS honeypot data summarized by the corresponding
  reporting helper.
- [Heralding](https://github.com/telekom-security/heralding) provides the
  credential-capture protocol emulation used for contained SMTP and SOCKS5
  observations.
- [Conpot](https://github.com/mushorg/conpot) provides the industrial-control
  system emulation used for contained SNMP observations.
- [SpiderFoot](https://github.com/smicallef/spiderfoot) provides the OSINT and
  infrastructure-enrichment framework discussed in the separated
  reconnaissance design.
- [CitrixHoneypot](https://github.com/MalwareTech/CitrixHoneypot), also
  packaged for T-Pot, provides the contained NetScaler/CVE-2019-19781-focused
  decoy discussed in the expanded VPS sensor set.
- [ADBHoney](https://github.com/huuck/ADBHoney) provides the Android Debug
  Bridge honeypot used for contained TCP/5555 observations.
- [Log4Pot](https://github.com/thomaspatzke/Log4Pot) provides the Log4Shell
  honeypot used for lookup-string analysis and guarded payload retrieval.
- [Elastic](https://www.elastic.co/) provides the private search and dashboard
  components used to visualize normalized event metadata.

Project names and trademarks belong to their respective owners. Inclusion here
does not imply affiliation, sponsorship, or endorsement. Users should consult
each upstream repository for its current documentation, license, and security
guidance.
