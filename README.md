# MiMo DevOps Assistant

MiMo DevOps Assistant is a Linux CLI diagnostic assistant powered by Xiaomi MiMo API.

## Problem
Small developers often manage servers alone. Debugging disk, memory, Docker, systemd, or network problems can be slow and risky, especially when copying random commands from the internet.

## Solution
This tool collects safe diagnostic output from the server and asks MiMo to explain the issue and suggest safe next steps.

## Core Features
- Disk usage diagnostics
- Memory diagnostics
- Top process summary
- MiMo-powered explanation
- Safe-action focused prompt

## Architecture
1. CLI runs safe read-only Linux commands
2. Output is combined into diagnostic context
3. MiMo analyzes server state
4. CLI prints recommended fixes

## Example Use Case
```bash
python devops_assistant.py diagnose
```
The assistant returns:
- likely cause
- safe cleanup commands
- commands to avoid
- next verification step

## Files
- `devops_assistant.py` — Typer CLI app
- `requirements.txt` — Python dependencies

## Roadmap
- Docker diagnostics
- systemd service analyzer
- log summarizer
- interactive fix mode
- server health report export

## Why Xiaomi MiMo
This project demonstrates MiMo as a practical coding and operations assistant for real Linux server workflows.

## Project Maturity
- MVP code available
- Architecture documented
- Roadmap documented
- CI configured
- MIT licensed

## Links
- [Architecture](ARCHITECTURE.md)
- [Roadmap](ROADMAP.md)
- [Examples](examples/basic.md)
