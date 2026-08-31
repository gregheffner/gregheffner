<h1 align="center">Greg Heffner</h1>

<p align="center"><b>Lead analyst, enterprise vulnerability management · risk-based decisions over raw severity</b></p>

<p align="center">
  <a href="https://greg.heffner.live"><img src="https://img.shields.io/badge/Nerdsense-greg.heffner.live-7AA2F7?style=for-the-badge&logo=hackthebox&logoColor=white" alt="website" /></a>
  <a href="https://greg.heffner.live/blog.html"><img src="https://img.shields.io/badge/Blog-learning_in_public-bb9af7?style=for-the-badge&logo=ghost&logoColor=white" alt="blog" /></a>
  <a href="mailto:main.plan5783@fastmail.com"><img src="https://img.shields.io/badge/Email-say_hi-c0caf5?style=for-the-badge&logo=maildotru&logoColor=white" alt="email" /></a>
</p>

<p align="center"><i>20+ years of learning in production. Still learning :)</i></p>

```yaml
role:    Lead Analyst, enterprise vulnerability management
arc:     20+ years · infrastructure → operations → security
leads:   triage, prioritization, remediation programs. Works the queue to keep the calls honest
style:   hands-on lead. Takes the ugly tickets, keeps a slice of the queue
method:  weigh exposure, mitigations, and accepted risk over raw scores
```

---

### About

I lead vulnerability analysis for an enterprise security team. Before that I spent two decades building and running the things I now defend: networks, Linux and Windows fleets, hypervisors, load balancers, disaster recovery. I've carried the pager, led the failovers, and sat on the code-red bridge calls at 3 AM. That history is the point: **I read vulnerability data the way an operator reads it**, because I was the operator.

I lead now, and I never left the keyboard. I take a slice of the queue because it keeps my prioritization calls honest, and when something breaks I join the incident instead of waiting for the summary. When I'm interested in something I go all in, and pressure doesn't change that: I'd rather be in the trenches with the team than learn about it secondhand. The trade I hold myself to: every hard problem I take becomes one an analyst owns next time.

The infrastructure years taught me what a scanner can't: which box is actually load-bearing, what a "critical" finding means on a host behind three layers of mitigation, and what breaks when you patch without a plan. The security work is where that pays off.

The newest layer is AI: Claude Code workflows, MCP servers, and agents doing the boring 80% (summarizing noise, drafting reports, chasing context) while I keep the 20% that needs judgment. The agent drafts, I hit send: trust earns autonomy, not the other way around. **The plan lives in code. Ansible, GitOps, agent workflows, not a wiki.** I've been learning in public on the blog since 2024, writing it down as I go.

> U.S. Army veteran. Network Switching Systems, attached to a Patriot Missile battalion. "Make the comms work, then make them resilient" was the first version of everything above.

---

### How I think about risk

CVSS tells you how bad a vulnerability *could* be. It doesn't tell you whether *you* should care. That gap is the whole job.

```text
CVE lands
  │
  ├─ In CISA KEV? Exploited in the wild?
  ├─ Reachable past the mitigations?
  ├─ On something that matters?
  └─ Compensating controls in place?
  │
  ├─► FIX NOW, out of cycle
  │     exploited + reachable + matters
  ├─► MITIGATE or ACCEPT, on the record,
  │     with a revisit date
  └─► NORMAL PATCH CYCLE
        everything else, and that's fine
```

- **Known-exploited beats theoretical-severity.** A KEV entry with a working exploit path outranks a CVSS 9.8 that nothing can reach.
- **Attack surface is a fact, not a feeling.** External exposure, open services, and actual reachability get verified, not assumed from a host list.
- **Accepted risk is a decision, written down.** Some findings you fix, some you mitigate, some you accept on the record and revisit. Silent backlog is none of those.
- **The patch cycle is a feature.** Most findings belong in the normal cadence. Reserving out-of-cycle urgency for things that earn it is what keeps the org listening when you do pull the alarm.

---

### Where the opinions get tested

The whole loop also runs at home, end to end: **Wazuh SIEM/XDR, Greenbone/OpenVAS, Trivy scanning every container image against CISA KEV daily, Ansible patching, Kubernetes + Argo CD GitOps on ESXi, Cloudflare WAF and Fail2Ban out front.** I'm scanner admin, analyst, patch team, and CAB all at once. Same method as work, where the scanners are Rapid7 and Qualys and the tickets live in ServiceNow. Nobody else to blame the process on here, though. Running total from the daily KEV scans: zero known-exploited vulnerabilities fleet-wide.

The lab is where the opinions get tested before they become advice.

---

### Where 20+ years went

| Era | What I ran | What it taught me |
| :-- | :-- | :-- |
| **Army: network comms** | Tactical networks under field conditions | Comms first, resilience second |
| **Infrastructure engineering** | Windows Server + RHEL fleets, VMware + Nutanix, load balancers, Active Directory | How systems actually fail, and where the bodies are buried |
| **Operations leadership** | Disaster recovery, failover design, code-red bridge calls | Calm is a skill; blast radius is a design input; downtime has a dollar sign |
| **Security: vulnerability management** | Triage and remediation across big fleets: Rapid7 InsightVM, Qualys, Tanium, CrowdStrike, ServiceNow Vulnerability Response + CMDB | Weigh severity against exposure and what the business can absorb, then make the call |
| **Now: leading from the keyboard** | Risk-based vuln program, agentic tooling, a team to grow | Stay hands-on, and teach the judgment instead of hoarding it |

---

### Tech I actually use

**Security Ops & Vuln Mgmt**

![Greenbone](https://img.shields.io/badge/Greenbone_%2F_OpenVAS-4C9A2A?style=for-the-badge)
![Wazuh](https://img.shields.io/badge/Wazuh_XDR-3A86FF?style=for-the-badge)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aquasecurity&logoColor=white)
![Cloudflare WAF](https://img.shields.io/badge/Cloudflare_WAF-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)

**AI & Agents**

![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-000000?style=for-the-badge)
![Windsurf](https://img.shields.io/badge/Windsurf-0B9E8E?style=for-the-badge&logo=windsurf&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-74AA9C?style=for-the-badge)
![MCP](https://img.shields.io/badge/MCP_servers-6E56CF?style=for-the-badge&logo=modelcontextprotocol&logoColor=white)

**Daily rotation:** dynamic workflows, custom agents, skills. Different tools, same rule: the agent drafts, I hit send.

**Infrastructure & Automation** *(the foundation everything sits on)*

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo_CD_/_GitOps-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![VMware](https://img.shields.io/badge/VMware_ESXi-607078?style=for-the-badge)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

**Languages:** Python · PowerShell · Bash · SQL · SPL (Splunk)

<details>
<summary><b>The enterprise toolbox</b> · ServiceNow, Splunk, Rapid7, Qualys, Tanium, CrowdStrike, Palo Alto, Active Directory, Azure, and about 60 more from the day jobs</summary>

*The badges above are the daily drivers. The rest of the inventory, grouped by what it does.*

**Observability & reporting** · Splunk + ITSI (dashboards, AD auditing, agent health, alerting), Datadog (APM, dashboards, change tracking), AppDynamics, Zenoss, SolarWinds Orion, NETSCOUT nGeniusONE, LiveNX, Catchpoint, Power BI

**Vulnerability management** · Rapid7 InsightVM, Qualys, Veracode

**Endpoint & EDR** · CrowdStrike Falcon, Tanium, McAfee ePO, Symantec Endpoint Protection

**Network & edge** · Palo Alto (Panorama, AutoFocus, firewall APIs), AlgoSec, Cisco ISE, Cisco Talos, Infoblox Grid Manager, Cradlepoint, Ubiquiti UniFi, Akamai

**Identity, certs & secrets** · Active Directory + Group Policy, Okta, NetIQ Identity Manager + eDirectory, Entrust certificate services, HashiCorp Vault

**Servers & virtualization** · Windows Server, RHEL, VMware vSphere + vCenter + ESXi, Nutanix Prism Central, Ansible Tower, NetBackup OpsCenter, Snow License Manager, IBM ILMT. The whole life of a box: build, patch, back up, test recovery, decommission, hand off. Pager included.

**ITSM & collaboration** · ServiceNow (CMDB, vulnerability response, build/decommission workflows, ticket-routing automation), Jira, Confluence, Bitbucket, SharePoint, AuditBoard

**Cloud** · AWS, Azure

**Glue** · REST + vendor API integrations, JavaScript + DataviewJS, YAML/JSON/TOML, automated reporting

</details>

---

### What I'm working on in 2026

| Focus | What I'm doing with it |
| :-- | :-- |
| **Risk-based triage at machine speed** | Claude Code *dynamic workflows* that read a finding, cross-reference CISA KEV + ATT&CK + actual exposure, and hand back a decision (fix now, mitigate, or normal cycle) instead of a wall of CVEs. |
| **Cheaper agents** | Pushing knowledge *down the stack* into skills and subagents so the expensive model only runs on judgment. *Tokens are money.* |
| **MCP everywhere** | Scanners, SIEM, dashboards and ticketing wired into agents over Model Context Protocol, so context comes to the model instead of me copy-pasting it. |
| **False-positive economics** | A finding that isn't real still costs analyst time. One raw lab scan: **74% false positives, every single "critical" included**, mostly backport-blind version matching. Building classification that proves what's actually running before anything pages a human. |

---

### From the blog

> A lab journal, not a brag sheet. Half practitioner notes, half beginner explainers, because teaching a thing is how I find out whether I actually learned it. Newest first.

| Post | What's in it |
| :-- | :-- |
| [**Fable 5 Weekend Projects**](https://greg.heffner.live/blog/fable-5-weekend-projects) | What a new model generation changes in real agent workflows |
| [**Machine-Speed Triage: Compressing MTTR with Claude Code Dynamic Workflows**](https://greg.heffner.live/blog/machine-speed-triage) | SOC triage automation · CISA KEV · MITRE ATT&CK |
| [**Push the Knowledge Down the Stack: Cheaper Agents Through Skills**](https://greg.heffner.live/blog/knowledge-down-the-stack) | Token economics · skills · subagents |
| [**Nessus & Wazuh: Watching the Watchers at Home**](https://greg.heffner.live/blog/nessus-and-wazuh) | Vuln scanning + SIEM/XDR in a home lab · Nessus since retired for Greenbone; the post documents its era |
| [**Claude Agents: The 7 Building Blocks**](https://greg.heffner.live/blog/claude-agent-building-blocks) | The pieces an agent system is actually made of |
| [**Why Claude Code Wanders in Big Repos (And Three Fixes)**](https://greg.heffner.live/blog/claude-code-big-repos) | Keeping agents on-task in large codebases |
| [**ActionCheck: The Terminal Dashboard That Knows Your CI/CD**](https://greg.heffner.live/blog/actioncheck) | Building a security-focused CI/CD TUI |

📖 **[Read the full index →](https://greg.heffner.live/blog.html)**

---

### Repos worth a look

*The automation substrate the security work runs on.*

| Repo | What it does |
| :-- | :-- |
| [**audits**](https://github.com/gregheffner/audits) | Security/compliance audit scripting |
| [**ansible-collection-ubuntu-patching**](https://github.com/gregheffner/ansible-collection-ubuntu-patching) | Fleet patching: apt/snap/brew, serial k8s drain-reboot |
| [**action-check**](https://github.com/gregheffner/action-check) | Security-focused CI/CD terminal dashboard |
| [**claude-skill-builder**](https://github.com/gregheffner/claude-skill-builder) | Scaffolding Claude Code skills |
| [**k8-patchNbounce**](https://github.com/gregheffner/k8-patchNbounce) | Patch + bounce Kubernetes nodes safely |
| [**cicd**](https://github.com/gregheffner/cicd) | Argo CD / GitOps automation for Kubernetes |
| [**playbooks**](https://github.com/gregheffner/playbooks) | Multi-platform Ansible: Ubuntu, Windows, Kali, macOS |
| [**k8Backup**](https://github.com/gregheffner/k8Backup) | Back up every Kubernetes resource type |

---

### Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=gregheffner&show_icons=true&theme=tokyonight&hide_border=true" alt="stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=gregheffner&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="top langs" />
</p>

---

<p align="center"><i>Still shipping. Still learning :)</i></p>
<p align="center">
  <a href="https://greg.heffner.live">website</a> ·
  <a href="https://greg.heffner.live/blog.html">blog</a> ·
  <a href="https://github.com/gregheffner">github</a> ·
  <a href="mailto:main.plan5783@fastmail.com">email</a>
</p>
