<!-- ░░ header ░░ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:0d1117,55:0f3d3a,100:1dc7a5&text=MehdiDev&fontColor=e6fffa&fontSize=64&fontAlignY=36&desc=builds%20across%20the%20whole%20stack%20%E2%80%94%20from%20kernels%20of%20math%20to%20kubernetes&descSize=16&descAlignY=58&animation=fadeIn" width="100%" alt="MehdiDev"/>
</p>

<p align="center">
  <a href="https://github.com/mehdii000">
    <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=1DC7A5&center=true&vCenter=true&width=640&height=40&lines=Kubernetes+controllers+for+Minecraft+fleets;Local-first+AI+agents+in+Rust+%26+Python;Neural+networks+from+scratch+in+C;Reverse-engineering+sketchy+Android+TV+boxes;Compilers%2C+parsers+%26+tiny+languages;btw%2C+I+use+CachyOS+%F0%9F%90%A7" alt="what I do"/>
  </a>
</p>

<p align="center">
  <a href="https://mehdidev.xyz/"><img src="https://img.shields.io/badge/mehdidev.xyz-0d1117?style=for-the-badge&logo=googlechrome&logoColor=1dc7a5" alt="website"/></a>
  <img src="https://img.shields.io/badge/CachyOS-0d1117?style=for-the-badge&logo=cachyos&logoColor=1dc7a5" alt="CachyOS"/>
  <img src="https://img.shields.io/badge/Hyprland-0d1117?style=for-the-badge&logo=hyprland&logoColor=1dc7a5" alt="Hyprland"/>
  <img src="https://komarev.com/ghpvc/?username=mehdii000&style=for-the-badge&color=1dc7a5&label=VISITORS" alt="profile views"/>
</p>

<br/>

## `$ whoami`

<table>
<tr>
<td width="56%" valign="top">

Hey, I'm **Mehdi** 👋 — a developer who can't stay on one layer of the stack.

One week I'm writing a **Go controller that keeps a warm pool of Minecraft servers** alive on Kubernetes; the next I'm training a **neural net in plain C** with nothing but matrices and backprop, or building a **Rust agent harness** that talks to models running on my own machine.

I like tools that are **local-first, private, and fast** — no cloud account, no telemetry, no nonsense. I also like fixing things for real people: I built a **one-button Arabic TV launcher for my grandmother** and dug an infected Android TV box apart to get it clean again.

- 🔭 Right now: **Planck** (local agent harness) and **nbai** (Android ↔ Linux bridge)
- 🌱 Digging into: k8s operators, compilers, reverse engineering
- 🎮 Long-time Minecraft / Skyblock modder
- 💬 Ask me about: Linux, Go, self-hosting, why your distro should be CachyOS

</td>
<td width="44%" valign="top">

```fish
mehdi@cachyos ~> fastfetch
  ╭──────────────────────────╮
  │  mehdi @ cachyos         │
  ╰──────────────────────────╯
  os       CachyOS x86_64
  kernel   linux-cachyos
  wm       Hyprland (wayland)
  shell    fish + atuin
  term     ghostty
  editor   zed
  git      lazygit
  monitor  btop
  ai       ollama (local)
  langs    ts go py rust c
  status   ▓▓▓▓▓▓▓▓▓░ shipping
```

</td>
</tr>
</table>

## 🐧 Daily driver: CachyOS

<p>
  <img align="right" src="https://cdn.simpleicons.org/cachyos/1dc7a5" width="72" alt="CachyOS logo"/>
</p>

Arch underneath, but tuned: **x86-64-v3/v4 optimised packages**, a BORE-scheduled kernel, and sane defaults out of the box. It's fast, it stays out of my way, and it lets me tinker as deep as I want. Paired with **Hyprland**, **Ghostty** and **fish**, it's the cleanest dev setup I've had.

<br clear="right"/>

## 🛠️ Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,go,py,rust,c,cpp,java,kotlin,js&theme=dark&perline=9" alt="languages"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,tailwind,vite,astro,godot&theme=dark&perline=9" alt="frameworks"/>
  <br/><br/>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,githubactions,linux,arch,bash,git,cmake,obsidian&theme=dark&perline=9" alt="tools"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Ollama-111?style=flat-square&logo=ollama&logoColor=white"/>
  <img src="https://img.shields.io/badge/Zed-111?style=flat-square&logo=zedindustries&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ghostty-111?style=flat-square&logo=ghostty&logoColor=white"/>
  <img src="https://img.shields.io/badge/fish-111?style=flat-square&logo=fishshell&logoColor=white"/>
  <img src="https://img.shields.io/badge/Hyprland-111?style=flat-square&logo=hyprland&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ghidra-111?style=flat-square"/>
  <img src="https://img.shields.io/badge/scrcpy%20%2F%20ADB-111?style=flat-square&logo=android&logoColor=white"/>
  <img src="https://img.shields.io/badge/PaperMC-111?style=flat-square"/>
</p>

## 🚀 Things I've built

<table>
<tr>
<td width="50%" valign="top">

### 📱 [nbai](https://github.com/mehdii000/nbai)
<sub>Rust · Linux · Android</sub><br/>
**N**ot **B**uying **A**n **i**Phone. Keeps your Android phone wired into your Linux desktop over authenticated Wireless ADB — scrcpy mirroring on demand and native notifications. No cloud, no LAN listener.

</td>
<td width="50%" valign="top">

### ⛏️ [RedstoneKube](https://github.com/mehdii000/RedstoneKube)
<sub>Go · Kubernetes · PaperMC</sub><br/>
Disposable Minecraft minigames on k8s. A stdlib-only Go controller keeps warm pools of game pods, registers them with a custom Velocity proxy, recycles them, and serves a live metrics dashboard.

</td>
</tr>
<tr>
<td valign="top">

### 🤖 [Planck](https://github.com/mehdii000/Planck)
<sub>Rust · TUI · Local LLMs</sub><br/>
A fast, local-first agent harness for Ollama, llama.cpp, LM Studio — anything OpenAI-compatible. Full-screen TUI, model picker, safe/auto/yolo modes.

</td>
<td valign="top">

### 🧠 [exLatticeV2](https://github.com/mehdii000/exLatticeV2)
<sub>C · ML from scratch</sub><br/>
A matrix-based neural network in pure C — forward pass, backprop and training loop with zero dependencies. Because you only really get it once you write it yourself.

</td>
</tr>
<tr>
<td valign="top">

### 📺 [arabic-tv-home](https://github.com/mehdii000/arabic-tv-home)
<sub>Java · Android TV</sub><br/>
A one-button Arabic Android TV launcher built for my grandmother, with local weather and tested on the real device.

</td>
<td valign="top">

### 🔬 [x96q-recovery-research](https://github.com/mehdii000/x96q-recovery-research)
<sub>Python · Reverse engineering</sub><br/>
Evidence-led recovery of an infected X96Q Android TV box, plus an experimental, version-pinned guard against Cobalt video-ad loaders.

</td>
</tr>
</table>

<details>
<summary><b>📦 More projects</b> <sub>(click to expand)</sub></summary>
<br/>

| Project | Stack | What it is |
|---|---|---|
| [EAMLCompiler](https://github.com/mehdii000/EAMLCompiler) | C++ | A tiny markup language with reusable components that compiles to HTML/CSS |
| [memath-parser](https://github.com/mehdii000/memath-parser) | C++ | Mathematical expression parsing toolkit |
| [SuperiorAgent](https://github.com/mehdii000/SuperiorAgent) | Python | Modular, session-aware AI agent with dynamic tool calling (Ollama / Qwen) |
| [SocialPlatform](https://github.com/mehdii000/SocialPlatform) | TS · Python · Docker | Full-stack, multi-container social network |
| [exLattice](https://github.com/mehdii000/exLattice) | C | The educational v1 feed-forward network |
| [localP2PChat](https://github.com/mehdii000/localP2PChat) | Go | Peer-to-peer chat on the local network |
| [inventory-hub](https://github.com/mehdii000/inventory-hub) | TypeScript | Data processor and analytics engine |
| [BadAddons](https://github.com/mehdii000/BadAddons) | Java | Hypixel Skyblock QoL mod |

</details>

<details>
<summary><b>🗺️ How my brain is wired</b> <sub>(click to expand)</sub></summary>
<br/>

```mermaid
mindmap
  root((Mehdi))
    Infra
      Kubernetes controllers
      Minecraft fleets
      Docker
      Self-hosting
    AI
      Local LLM agents
      Ollama
      Neural nets in C
    Systems
      Rust tools
      Compilers & parsers
      Reverse engineering
    Product
      Full-stack TypeScript
      Go backends
      Android TV apps
    Desktop
      CachyOS
      Hyprland
      fish + ghostty
```

</details>

## 📊 Stats

<p align="center">
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=mehdii000&theme=github_dark" alt="profile details"/>
</p>
<p align="center">
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=mehdii000&theme=github_dark" alt="repos per language"/>
  <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=mehdii000&theme=github_dark" alt="most commit language"/>
</p>
<p align="center">
  <img height="170" src="https://streak-stats.demolab.com/?user=mehdii000&background=0d1117&border=1dc7a5&ring=1dc7a5&fire=1dc7a5&currStreakLabel=1dc7a5&sideLabels=c9d1d9&currStreakNum=e6fffa&sideNums=e6fffa&dates=8b949e&stroke=30363d&border_radius=10" alt="streak"/>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mehdii000/mehdii000/output/github-snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mehdii000/mehdii000/output/github-snake.svg"/>
    <img alt="contribution snake" src="https://raw.githubusercontent.com/mehdii000/mehdii000/output/github-snake-dark.svg"/>
  </picture>
</p>

<!-- ░░ footer ░░ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=110&section=footer&color=0:1dc7a5,45:0f3d3a,100:0d1117" width="100%" alt=""/>
</p>
