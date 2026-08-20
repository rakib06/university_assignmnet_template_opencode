# Quick Start Guide

Get up and running with the assignment template in 5 minutes.

---

## Prerequisites

### 1. WSL (Windows Subsystem for Linux)

All tools run inside WSL. Install it first:

```powershell
# In PowerShell (Run as Administrator)
wsl --install
```

Restart your PC, then open the **Ubuntu** app from the Start menu to complete setup.

> **Why WSL?** Python, Node.js, opencode, and all build tools run natively inside the Linux environment. Access your Windows files via `/mnt/c/`.

### 2. Install tools inside WSL

Open the **Ubuntu terminal** and run:

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Python
sudo apt install -y python3 python3-pip

# Node.js
sudo apt install -y nodejs npm

# opencode (see https://opencode.ai for install instructions)

# Python packages
pip install python-docx Pillow
```

---

## Setup

### 1. Copy the template

Windows files are accessible under `/mnt/c/`. From the Ubuntu terminal:

```bash
# Example: copy from a Windows folder to your home directory
cp -r "/mnt/c/Users/you/Desktop/assignment-template/" ~/my-assignment/
cd ~/my-assignment/
```

Or work directly from the Windows path:

```bash
cd "/mnt/c/Users/you/Desktop/assignment-template/"
```

### 2. Run the setup script

```bash
python3 setup.py
```

Enter your details (name, ID, course, assignment title, etc.). This generates:
- `templates/report_config.json` — Your metadata
- `templates/task.md` — Assignment task description
- `.opencode/` — Plugin structure with dependencies

### 3. Open in opencode

```bash
opencode
```

Everything loads automatically — plugins, tools, skills.

---

## Workflow

### Write Code

Tell the AI:
```
Write the code for my assignment. Read templates/task.md for requirements.
```

### Build & Run

Use your development tool to build and run the code. Check your assignment brief for the expected build and run commands.

### Take Screenshots

Save PNG files to `screenshots/`:

| File | What to capture |
|---|---|
| `code_view.png` | Top half of your code |
| `code_view_2.png` | Bottom half of your code |
| `compile.png` | Compilation/build output |
| `run.png` | Run button (optional) |
| `run_start.png` | Console prompt |
| `execution_output.png` | Final console output |
| `error1.png` | Error message (if any) |

### Generate Report

```bash
python3 assets/generate_report.py
```

Output: `report_final.docx` in your project folder.

### Review & Submit

Open the DOCX in Word/LibreOffice, verify screenshots are embedded, and submit.

---

## Common Prompts

| Task | Prompt |
|---|---|
| Write code | `Write the code for my assignment. Read templates/task.md.` |
| Fix error | `I got this error: [paste]. Please fix the code.` |
| Generate report | `Generate the DOCX report for my assignment.` |
| Take screenshot | `Take a screenshot of the current screen` |
| Full workflow | `Help me complete my full assignment end-to-end.` |

---

## Troubleshooting

- **"Configuration file not found"** → Run `python3 setup.py`
- **Images not in report** → Check files are in `screenshots/` and named correctly
- **Plugins not loading** → Run `cd .opencode && npm install`
- **Screenshot tool fails** → Ensure Windows + PowerShell is accessible from WSL

---

For full details, see [README.md](README.md).
