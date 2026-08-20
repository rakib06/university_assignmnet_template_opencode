#!/usr/bin/env python3
"""
Assignment Template Setup Script
================================
Interactive setup for new university assignments using opencode.

Run: python3 setup.py
It will ask for your details and generate all required files.
"""

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def ask(question, default=None, required=False):
    """Ask a question and return the answer."""
    suffix = f" [{default}]" if default else ""
    suffix += " (required)" if required else ""
    while True:
        answer = input(f"  {question}{suffix}: ").strip()
        if answer:
            return answer
        if default:
            return default
        if not required:
            return ""
        print("    This field is required. Please enter a value.")


def create_opencode_structure():
    """Create the .opencode directory structure with plugins, tools, scripts, skills."""
    opencode_dir = os.path.join(BASE_DIR, ".opencode")

    # Create directories
    dirs = [
        os.path.join(opencode_dir, "plugins"),
        os.path.join(opencode_dir, "scripts"),
        os.path.join(opencode_dir, "tools"),
        os.path.join(opencode_dir, "skills", "assignment-mode"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # ── package.json ─────────────────────────────────────────────────
    pkg_path = os.path.join(opencode_dir, "package.json")
    if not os.path.exists(pkg_path):
        with open(pkg_path, "w") as f:
            json.dump({"dependencies": {"@opencode-ai/plugin": "1.18.18"}}, f, indent=2)
        print(f"  [OK] Created: {pkg_path}")

    # ── .gitignore ───────────────────────────────────────────────────
    gi_path = os.path.join(opencode_dir, ".gitignore")
    if not os.path.exists(gi_path):
        with open(gi_path, "w") as f:
            f.write("node_modules\npackage.json\npackage-lock.json\nbun.lock\n.gitignore\n")
        print(f"  [OK] Created: {gi_path}")

    # ── plugins/interaction-archiver.ts ──────────────────────────────
    plugin_path = os.path.join(opencode_dir, "plugins", "interaction-archiver.ts")
    if not os.path.exists(plugin_path):
        # Copy from template source if available
        src = os.path.join(BASE_DIR, ".opencode", "plugins", "interaction-archiver.ts")
        if os.path.exists(src):
            shutil.copy2(src, plugin_path)
            print(f"  [OK] Copied: interaction-archiver.ts")
        else:
            print(f"  [WARN] interaction-archiver.ts not found, skipping")

    # ── plugins/README.md ────────────────────────────────────────────
    plugin_readme = os.path.join(opencode_dir, "plugins", "README.md")
    if not os.path.exists(plugin_readme):
        src = os.path.join(BASE_DIR, ".opencode", "plugins", "README.md")
        if os.path.exists(src):
            shutil.copy2(src, plugin_readme)
            print(f"  [OK] Copied: plugins/README.md")

    # ── scripts/screenshot.ps1 ───────────────────────────────────────
    ps1_path = os.path.join(opencode_dir, "scripts", "screenshot.ps1")
    if not os.path.exists(ps1_path):
        src = os.path.join(BASE_DIR, ".opencode", "scripts", "screenshot.ps1")
        if os.path.exists(src):
            shutil.copy2(src, ps1_path)
            print(f"  [OK] Copied: screenshot.ps1")
        else:
            print(f"  [WARN] screenshot.ps1 not found, skipping")

    # ── tools/screenshot.ts ──────────────────────────────────────────
    ts_path = os.path.join(opencode_dir, "tools", "screenshot.ts")
    if not os.path.exists(ts_path):
        src = os.path.join(BASE_DIR, ".opencode", "tools", "screenshot.ts")
        if os.path.exists(src):
            shutil.copy2(src, ts_path)
            print(f"  [OK] Copied: screenshot.ts")
        else:
            print(f"  [WARN] screenshot.ts not found, skipping")

    # ── skills/assignment-mode/SKILL.md ──────────────────────────────
    skill_path = os.path.join(opencode_dir, "skills", "assignment-mode", "SKILL.md")
    if not os.path.exists(skill_path):
        src = os.path.join(BASE_DIR, ".opencode", "skills", "assignment-mode", "SKILL.md")
        if os.path.exists(src):
            shutil.copy2(src, skill_path)
            print(f"  [OK] Copied: SKILL.md")
        else:
            print(f"  [WARN] SKILL.md not found, skipping")

    # ── Install dependencies ─────────────────────────────────────────
    print("  Installing .opencode dependencies...")
    try:
        subprocess.run(
            ["npm", "install"],
            cwd=opencode_dir,
            capture_output=True,
            timeout=60,
        )
        print(f"  [OK] npm install completed")
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print(f"  [WARN] npm not found or install timed out. Run manually: cd .opencode && npm install")


def main():
    print("=" * 60)
    print("  ASSIGNMENT TEMPLATE SETUP")
    print("  Configure your assignment workspace")
    print("=" * 60)
    print()

    config = {}

    # ── Required Fields ──────────────────────────────────────────────
    print("[1/3] Student Information")
    config["student_name"] = ask("Student Name", required=True)
    config["student_id"] = ask("Student ID", required=True)
    print()

    print("[2/3] Course Information")
    config["university"] = ask(
        "University Name",
        default="Bangladesh University of Professionals",
    )
    config["course_code"] = ask("Course Code (e.g., MCS2214)", required=True)
    config["course_name"] = ask("Course Name (e.g., Advanced Reverse Engineering)", required=True)
    config["assignment_title"] = ask("Assignment Title", required=True)
    config["platform"] = ask("Platform / Tool (e.g., VS Code, GCC, Python, emu8086)", default="")
    print()

    print("[3/3] Optional Details (press Enter to skip)")
    config["faculty_name"] = ask("Faculty Name")
    config["faculty_designation"] = ask("Faculty Designation (e.g., Associate Professor)")
    config["semester"] = ask("Semester (e.g., Spring 2026)")
    config["section"] = ask("Section (e.g., A)")
    config["submission_date"] = ask("Submission Date (e.g., August 20, 2026)")
    print()

    # ── Save Config ──────────────────────────────────────────────────
    config_path = os.path.join(BASE_DIR, "templates", "report_config.json")
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"[OK] Configuration saved to: {config_path}")

    # ── Generate task.md ─────────────────────────────────────────────
    task_path = os.path.join(BASE_DIR, "templates", "task.md")
    task_content = f"""# Assignment Task

**Title:** {config['assignment_title']}

## Student Information
- **Name:** {config['student_name']}
- **ID:** {config['student_id']}

## Course Information
- **Course:** {config['course_code']} - {config['course_name']}
- **University:** {config['university']}
"""
    if config.get("semester"):
        task_content += f"- **Semester:** {config['semester']}\n"
    if config.get("section"):
        task_content += f"- **Section:** {config['section']}\n"
    if config.get("faculty_name"):
        task_content += f"- **Faculty:** {config['faculty_name']}"
        if config.get("faculty_designation"):
            task_content += f", {config['faculty_designation']}"
        task_content += "\n"
    if config.get("submission_date"):
        task_content += f"- **Submission Date:** {config['submission_date']}\n"

    task_content += f"""
## Platform
- **Tool:** {config['platform']}

## Requirements
1. Develop the assigned program in {config['platform']}
2. Submit a report explaining:
   - Program logic
   - Assembly instructions used (if applicable)
   - Execution output with screenshots
"""
    with open(task_path, "w") as f:
        f.write(task_content)
    print(f"[OK] Task template saved to: {task_path}")

    # ── Create screenshots folder ────────────────────────────────────
    screenshots_dir = os.path.join(BASE_DIR, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    print(f"[OK] Screenshots folder ready: {screenshots_dir}")

    # ── Create .opencode structure ───────────────────────────────────
    print()
    print("Setting up .opencode/ structure...")
    create_opencode_structure()

    # ── Verify assets ────────────────────────────────────────────────
    logo_path = os.path.join(BASE_DIR, "assets", "bup_logo.png")
    report_gen = os.path.join(BASE_DIR, "assets", "generate_report.py")
    if os.path.exists(logo_path):
        print(f"[OK] University logo found: {logo_path}")
    else:
        print(f"[WARN] University logo not found at: {logo_path}")
        print("       Place your university logo as assets/bup_logo.png")
    if os.path.exists(report_gen):
        print(f"[OK] Report generator found: {report_gen}")
    else:
        print(f"[WARN] Report generator not found at: {report_gen}")

    # ── Done ─────────────────────────────────────────────────────────
    print()
    print("=" * 60)
    print("  SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("  Project structure:")
    print("    .opencode/           — plugins, tools, skills (auto-loaded)")
    print("    assets/              — report generator + university logo")
    print("    templates/           — task description + config")
    print("    screenshots/         — save screenshots here")
    print("    prompts/             — prompt examples")
    print()
    print("  Next steps:")
    print("  1. Open this folder in opencode")
    print("  2. Say: \"Write the code for my assignment\"")
    print("  3. Build, run, and test your code")
    print("  4. Take screenshots and save to screenshots/")
    print("  5. Say: \"Generate the DOCX report\"")
    print("  6. Review report_final.docx and submit")
    print()
    print("  To generate report manually:")
    print(f"    python3 assets/generate_report.py")
    print()


if __name__ == "__main__":
    main()
