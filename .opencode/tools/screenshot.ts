import { tool } from "@opencode-ai/plugin"
import { $ } from "bun"
import path from "node:path"
import fs from "node:fs/promises"

export default tool({
  description:
    "Take a screenshot of the Windows host desktop. Use this when visual inspection of the user's screen is necessary during implementation, debugging, or UI work. Do not use unnecessarily.",

  args: {
    mode: tool.schema
      .enum(["primary", "all"])
      .default("primary")
      .describe(
        "Capture the primary monitor or all connected monitors."
      ),
  },

  async execute(args, context) {
    const timestamp = new Date()
      .toISOString()
      .replace(/[:.]/g, "-")

    const screenshotDir = path.join(
      context.worktree,
      "screenshots"
    )

    await fs.mkdir(screenshotDir, {
      recursive: true,
    })

    const filename = `screen-${timestamp}.png`

    const linuxPath = path.join(
      screenshotDir,
      filename
    )

    const windowsScriptPath = await $`wslpath -w ${path.join(
      context.worktree,
      ".opencode",
      "scripts",
      "screenshot.ps1"
    )}`.text()

    const windowsOutputPath = await $`wslpath -w ${linuxPath}`.text()

    const script = windowsScriptPath.trim()
    const output = windowsOutputPath.trim()

    await $`powershell.exe -NoProfile -ExecutionPolicy Bypass -File ${script} -OutputPath ${output} -Mode ${args.mode}`

    await fs.access(linuxPath)

    const imageBuffer = await fs.readFile(linuxPath)

    const base64 = imageBuffer.toString("base64")

    return {
      title: `Windows screenshot: ${filename}`,

      output:
        `Screenshot captured successfully.\n` +
        `Mode: ${args.mode}\n` +
        `File: ${linuxPath}\n` +
        `The screenshot is attached for visual inspection.`,

      attachments: [
        {
          type: "file",
          mime: "image/png",
          url: `data:image/png;base64,${base64}`,
          filename,
        },
      ],
    }
  },
})
