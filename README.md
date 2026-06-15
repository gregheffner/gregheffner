<h1 align="center">Greg Heffner</h1>

<p align="center">
  <a href="https://greg.heffner.live">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=3200&pause=900&color=7AA2F7&center=true&vCenter=true&width=760&lines=Vulnerability+management+%2F+security+operations;Triage+%E2%86%92+prioritize+(KEV+%2B+ATT%26CK)+%E2%86%92+remediate+%E2%86%92+verify;AI+as+the+force+multiplier%2C+not+the+pilot;The+plan+lives+in+code.+Tokens+are+money." alt="typing banner" />
  </a>
</p>

<p align="center">
  <a href="https://greg.heffner.live"><img src="https://img.shields.io/badge/Nerdsense-greg.heffner.live-7AA2F7?style=for-the-badge&logo=hackthebox&logoColor=white" alt="website" /></a>
  <a href="https://greg.heffner.live/blog.html"><img src="https://img.shields.io/badge/Blog-learning_in_public-bb9af7?style=for-the-badge&logo=ghost&logoColor=white" alt="blog" /></a>
  <a href="mailto:main.plan5783@fastmail.com"><img src="https://img.shields.io/badge/Email-say_hi-c0caf5?style=for-the-badge&logo=maildotru&logoColor=white" alt="email" /></a>
  <img src="https://komarev.com/ghpvc/?username=gregheffner&style=for-the-badge&color=414868&label=PROFILE+VIEWS" alt="profile views" />
</p>

<p align="center"><i>made to learn and have fun. I'm still learning :)</i></p>

---

### About

I live in vulnerability data. The work is straightforward to say and hard to do: find what's exposed, figure out what actually matters, and drive it to fixed across messy real-world environments. I read scan output, chase down owners, track remediation until it closes, and turn raw findings into a plan someone can act on.

The newer half is leaning on AI to do the boring 80% faster — summarizing noise, drafting reports, accelerating research — while I keep the 20% that needs judgment. Deterministic glue holds the workflow together; the model fills the gaps where rules can't. Clean line between the two. **The plan lives in code.** I learn most of this in public and write it down as I go.

> U.S. Army veteran — network communications. That's where the "make the comms work, then make them resilient" habit started.

---

### What I work on

```text
  scan  →  triage  →  prioritize  →  remediate  →  verify  →  (repeat, faster)
   │         │            │              │            │
 Nessus   noise vs.    CISA KEV      Ansible at    re-scan +
 Wazuh    real risk    MITRE ATT&CK  scale         file-integrity
```

- **Vulnerability triage & remediation programs** — separating noise from real risk, tracking backlog to closed, writing findings up so engineering teams can act without a translator.
- **KEV / ATT&CK-driven prioritization** — patch what's being exploited now, not what scores highest on paper.
- **Remediation at scale** — Ansible patching across Ubuntu / Windows / Kubernetes, zero-downtime node reboots, GitOps.
- **Home SOC, run for real** — Nessus for scanning, Wazuh for SIEM/XDR, plus file-integrity monitoring, Fail2Ban, AbuseIPDB and a Cloudflare WAF out front. Watching the watchers.
- **AI as a force multiplier** — Claude Code dynamic workflows, MCP servers, skills and subagents to compress reporting and research. The model handles judgment; the glue handles everything else.

---

### Tech I actually use

**Security Ops & Vuln Mgmt**

![Nessus](https://img.shields.io/badge/Nessus-00A98F?style=for-the-badge)
![Wazuh](https://img.shields.io/badge/Wazuh_XDR-3A86FF?style=for-the-badge)
![CISA KEV](https://img.shields.io/badge/CISA_KEV-1F3A93?style=for-the-badge)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-C8102E?style=for-the-badge)
![Cloudflare WAF](https://img.shields.io/badge/Cloudflare_WAF-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![Fail2Ban](https://img.shields.io/badge/Fail2Ban-D32F2F?style=for-the-badge)
![AbuseIPDB](https://img.shields.io/badge/AbuseIPDB-1565C0?style=for-the-badge)

**AI & Agents**

![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Agent SDK](https://img.shields.io/badge/Claude_Agent_SDK-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Anthropic API](https://img.shields.io/badge/Anthropic_API-191919?style=for-the-badge&logo=anthropic&logoColor=white)
![MCP](https://img.shields.io/badge/MCP_servers-6E56CF?style=for-the-badge&logo=modelcontextprotocol&logoColor=white)
![Skills](https://img.shields.io/badge/Skills_%26_Subagents-8B5CF6?style=for-the-badge)

**Infrastructure & Automation**

![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo_CD_/_GitOps-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge)

---

### Currently exploring — 2026

The stuff I'm actively building and writing about right now:

| Focus | What I'm doing with it |
| :-- | :-- |
| **Machine-speed triage** | Claude Code *dynamic workflows* that read a finding, cross-reference CISA KEV + MITRE ATT&CK, and hand back next steps instead of a wall of CVEs. Cuts MTTR without handing over the wheel. |
| **KEV-driven prioritization** | Findings ranked by *known exploited* first, ATT&CK technique second. Severity score alone lies — exploitation in the wild doesn't. |
| **Cheaper agents** | Pushing knowledge *down the stack* into skills and subagents so the expensive model only runs on the judgment. *Tokens are money. Start acting like it.* |
| **MCP servers** | Wiring scanners, ticketing and dashboards into agents over Model Context Protocol so context comes to the model instead of me copy-pasting it. |
| **Token budgeting** | Context as a resource with a price tag. `CLAUDE.md`, scoped tools, lean prompts, the right model for the job. |

---

### From the blog

> Practical, hands-on, no-fluff. A lab journal, not a brag sheet. Newest first.

| Post | What's in it |
| :-- | :-- |
| [**Machine-Speed Triage: Compressing MTTR with Claude Code Dynamic Workflows**](https://greg.heffner.live/image/pages/2026/June/AgenticMTTR.html) | SOC triage automation · CISA KEV · MITRE ATT&CK |
| [**Push the Knowledge Down the Stack: Cheaper Agents Through Skills**](https://greg.heffner.live/image/pages/2026/June/TokensDownTheStack.html) | Token economics · skills · subagents |
| [**Nessus & Wazuh: Watching the Watchers at Home**](https://greg.heffner.live/image/pages/2026/May/NessusandWazuh.html) | Vuln scanning + SIEM/XDR in a home lab |
| [**Claude Agents: The 7 Building Blocks**](https://greg.heffner.live/image/pages/2026/May/ClaudeSkills.html) | The pieces an agent system is actually made of |
| [**Why Claude Code Wanders in Big Repos (And Three Fixes)**](https://greg.heffner.live/image/pages/2026/May/ClaudeBigRepo.html) | Keeping agents on-task in large codebases |
| [**ActionCheck: The Terminal Dashboard That Knows Your CI/CD**](https://greg.heffner.live/image/pages/2026/Jan/actioncheck.html) | Building a security-focused CI/CD TUI |

📖 **[Read the full index →](https://greg.heffner.live/blog.html)**

---

### Featured repos

<table>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/gregheffner/audits">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=gregheffner&repo=audits&theme=tokyonight&hide_border=true" alt="audits" />
</a>

</td>
<td width="50%" valign="top">

<a href="https://github.com/gregheffner/ansible-collection-ubuntu-patching">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=gregheffner&repo=ansible-collection-ubuntu-patching&theme=tokyonight&hide_border=true" alt="ansible-collection-ubuntu-patching" />
</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/gregheffner/ansible-role-k8-maintenance">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=gregheffner&repo=ansible-role-k8-maintenance&theme=tokyonight&hide_border=true" alt="ansible-role-k8-maintenance" />
</a>

</td>
<td width="50%" valign="top">

<a href="https://github.com/gregheffner/action-check">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=gregheffner&repo=action-check&theme=tokyonight&hide_border=true" alt="action-check" />
</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="https://github.com/gregheffner/claude-skill-builder">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=gregheffner&repo=claude-skill-builder&theme=tokyonight&hide_border=true" alt="claude-skill-builder" />
</a>

</td>
<td width="50%" valign="top">

<a href="https://github.com/gregheffner/k8-patchNbounce">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=gregheffner&repo=k8-patchNbounce&theme=tokyonight&hide_border=true" alt="k8-patchNbounce" />
</a>

</td>
</tr>
</table>

#### More worth a look

| Repo | What it does |
| :-- | :-- |
| [**cicd**](https://github.com/gregheffner/cicd) | Argo CD / GitOps automation for Kubernetes |
| [**playbooks**](https://github.com/gregheffner/playbooks) | Multi-platform Ansible — Ubuntu, Windows, Kali, macOS |
| [**ansible-role-windows-update**](https://github.com/gregheffner/ansible-role-windows-update) | Windows Update patching, automated |
| [**k8Backup**](https://github.com/gregheffner/k8Backup) | Back up every Kubernetes resource type |

---

### Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=gregheffner&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=gregheffner&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="top langs" />
</p>
<p align="center">
  <img height="165" src="https://streak-stats.demolab.com?user=gregheffner&theme=tokyonight&hide_border=true" alt="streak" />
</p>
<p align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=gregheffner&theme=tokyonight&no-frame=true&no-bg=true&margin-w=4&row=1&column=7" alt="trophies" />
</p>

---

<p align="center"><i>Still learning. Still shipping. The plan lives in code — the rest is judgment. :)</i></p>
<p align="center">
  <a href="https://greg.heffner.live">website</a> ·
  <a href="https://greg.heffner.live/blog.html">blog</a> ·
  <a href="https://github.com/gregheffner">github</a> ·
  <a href="mailto:main.plan5783@fastmail.com">email</a>
</p>
