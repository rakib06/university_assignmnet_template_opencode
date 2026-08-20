# Prompt Examples for Assignment Mode

Copy and paste these prompts into opencode when working on your assignment.

---

## 1. Write Code for Assignment

```
Write the code for my assignment. Read templates/task.md for the requirements.
The assignment is about [brief description]. Use [platform/language].
```

## 2. Write Assembly Code (emu8086)

```
Write an 8086 assembly program for emu8086 that [describe what it should do].
The program should:
- Accept user input at runtime
- Display results on screen
- Use proper comments
- Follow emu8086-compatible syntax (ORG 100h, .DATA, .CODE)
```

## 3. Generate DOCX Report

```
Generate the DOCX report for my assignment.
Run: python3 assets/generate_report.py
Make sure all screenshots from screenshots/ folder are embedded.
```

## 4. Explain Code Segments

```
Explain each segment of my code in detail with academic tone.
Break the code into logical segments and for each segment provide:
- The code snippet
- Line numbers
- Detailed explanation of what it does and why
```

## 5. Fix Compilation Error

```
I got this error when building my code in emu8086:
[paste error here]
Please fix the code and explain what was wrong.
```

## 6. Fix Runtime Error

```
The code compiles but gives wrong output.
Input: [what you entered]
Expected: [what you expected]
Got: [what actually appeared]
Please fix the code.
```

## 7. Add More Detail to Report

```
The report needs more detail in section [X].
Please expand the explanation with deeper academic analysis.
```

## 8. Verify Output Correctness

```
Verify if this output is correct:
[paste output]
For input N = [value], the expected sum should be [value].
Is the program working correctly?
```

## 9. Take Screenshots and Embed

```
I have saved screenshots in the screenshots/ folder.
Please generate the report with these screenshots embedded.
Run: python3 assets/generate_report.py
```

## 10. Full Assignment Workflow (Start to Finish)

```
Help me complete my full assignment workflow:
1. Read templates/task.md for requirements
2. Write the code
3. Guide me to build and run it
4. Help me take the right screenshots
5. Generate the DOCX report
6. Review and finalize

Start with step 1.
```

## 11. Customize Report for Different Assignment Type

```
My assignment is not about assembly. It is about [Python/C/Java/network security/etc.].
Please adjust the report template accordingly:
- Replace "Assembly Instructions" with relevant section
- Adjust code explanation sections for [language]
- Keep the same academic formatting
```

## 12. Quick Report Regeneration

```
Regenerate the report. I updated the screenshots in the screenshots/ folder.
Run: python3 assets/generate_report.py
```
