# Assignment Mode — Agent Instructions

You are operating in **Assignment Mode** for a university coursework submission.

## Before Starting Any Task

1. **Load the assignment skill**: Read `.opencode/skills/assignment-mode/SKILL.md` for the complete workflow
2. Read `templates/report_config.json` for student/course metadata
3. Read `templates/task.md` for assignment requirements
4. Read `screenshots/` directory to see what screenshots exist

## Available Tools & Plugins

This project includes the following opencode extensions in `.opencode/`:

| Component | Location | Purpose |
|---|---|---|
| **Assignment Skill** | `.opencode/skills/assignment-mode/SKILL.md` | Workflow for assignment tasks |
| **Screenshot Tool** | `.opencode/tools/screenshot.ts` | Capture Windows desktop screenshots |
| **Screenshot Script** | `.opencode/scripts/screenshot.ps1` | PowerShell backend for screenshot capture |
| **Interaction Archiver** | `.opencode/plugins/interaction-archiver.ts` | Auto-archives all prompts and responses |

### Using the Screenshot Tool

To capture a screenshot of the user's Windows desktop:
```
Use the screenshot tool to capture the current screen
```
The tool saves screenshots to `screenshots/` as PNG files with timestamps.

## Code Writing Rules

- Write clean, well-commented code
- Use meaningful variable names
- Add a program header with: title, student name, ID, course, platform
- Follow standard conventions for the language being used

## Report Generation Rules

When generating a DOCX report, ALWAYS use Python:

```bash
python3 assets/generate_report.py
```

**Never** use other methods to generate the report. The Python script reads configuration from `templates/report_config.json` and embeds screenshots from `screenshots/`.

### Formatting Standards
- **Font:** Times New Roman, 12pt body
- **Color:** Black (no colored headings)
- **Line spacing:** 1.5
- **Code blocks:** Consolas, 8-9pt
- **Tone:** Formal academic language with depth

### Report Structure (Required Sections)
1. **Cover Page** — University logo, title, course, name, ID, semester, faculty
2. **Table of Contents**
3. **Introduction** — Background, objective, scope
4. **Program Logic** — Step-by-step algorithm
5. **Source Code Listing** — Full code with line numbers
6. **Detailed Code Explanation** — Segment-by-segment breakdown (code + explanation for each block)
7. **Instructions Reference** — Table of all instructions/commands used
8. **Screenshots** — Embedded images from `screenshots/` folder with figure captions
9. **Expected Output** — Textual sample run
10. **Conclusion** — Learning outcomes, summary
11. **References**

### Screenshot Handling
- Screenshots go in the `screenshots/` folder
- Use the screenshot tool (`.opencode/tools/screenshot.ts`) to capture screens
- Supported names: `code_view.png`, `code_view_2.png`, `compile.png`, `run.png`, `run_start.png`, `execution_output.png`, `error1.png`
- The report generator auto-embeds all PNG files found
- Images are scaled to fit within page margins with preserved aspect ratio

## When User Says "Generate Report"

1. Run: `python3 assets/generate_report.py`
2. Output is saved as `report_final.docx`
3. Tell user to review and submit

## When User Asks to Fix Errors

1. Read the error message carefully
2. Identify the root cause
3. Fix the code
4. Explain what was wrong and how it was fixed
5. Ask user to rebuild and retest

## When User Asks to Take Screenshot

1. Use the screenshot tool to capture the current screen
2. The tool automatically saves to `screenshots/` with a timestamp
3. Ask user to rename the file if needed (e.g., `code_view.png`)

## Academic Integrity

- Always use the student's own work
- Explain concepts but do not write entire assignments for them without effort
- Encourage understanding of the code
- Report should reflect the student's learning
