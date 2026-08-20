# Interaction Archiver Plugin

Automatically archives all user prompts, assistant responses, and plan/todo updates from OpenCode sessions.

## Features

- **User prompt capture** — every message sent to OpenCode is logged
- **Assistant response capture** — AI responses are archived alongside prompts
- **Plan/todo tracking** — task list changes are recorded
- **Session lifecycle** — session creation, idle, and error events are captured
- **Append-only logs** — historical entries are never overwritten
- **Monthly bucketing** — archives organized by `YYYY/MM/day_XX_to_XX/`

## Archive Structure

```
.opencode-archive/
└── 2026/
    └── 08/
        ├── day_01_to_10/
        │   ├── prompts.log          # JSONL machine-readable log
        │   └── prompt_and_plan.md   # Human-readable markdown
        ├── day_11_to_20/
        │   ├── prompts.log
        │   └── prompt_and_plan.md
        └── day_21_to_31/
            ├── prompts.log
            └── prompt_and_plan.md
```

## File Formats

### prompts.log (JSONL)

Each line is a JSON object with event metadata:

```json
{"event":"user_prompt","timestamp":"2026-08-19T22:45:00.000Z","sessionID":"abc123","agent":"plan","messageID":"msg_456","prompt":"Check if MCP servers are running"}
{"event":"assistant_response","timestamp":"2026-08-19T22:45:05.000Z","sessionID":"abc123","messageID":"msg_789","content":"All 4 local MCP servers are running..."}
{"event":"todo_updated","timestamp":"2026-08-19T22:46:00.000Z","properties":{...}}
```

### prompt_and_plan.md

Chronological markdown with timestamps and session context:

```markdown
## User Prompt — Agent: plan

**Timestamp:** 2026-08-19T22:45:00.000Z

**Session ID:** `abc123`
**Message ID:** `msg_456`

### Prompt

Check if MCP servers are running

---
```

## Event Types Captured

| Event | Source | Description |
|-------|--------|-------------|
| `user_prompt` | `chat.message` hook | User message to OpenCode |
| `assistant_response` | `event` hook | AI assistant reply |
| `session_created` | `event` hook | New session started |
| `session_idle` | `event` hook | Session became idle |
| `session_error` | `event` hook | Session error occurred |
| `todo_updated` | `event` hook | Plan/task list changed |

## Installation

The plugin is automatically loaded from `.opencode/plugins/` at OpenCode startup. No configuration required.

To disable: rename or delete `.opencode/plugins/interaction-archiver.ts`.

## Technical Details

- **SDK**: `@opencode-ai/plugin` v1.18.18 (v1 classic API)
- **Hooks used**: `chat.message` (user prompts), `event` (lifecycle/responses)
- **File I/O**: Synchronous `fs` operations for reliability
- **Bucket logic**: Days 1-10, 11-20, 21-31 mapped to monthly subdirectories
