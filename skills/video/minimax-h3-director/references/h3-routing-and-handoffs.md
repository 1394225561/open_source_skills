# H3 Routing and Handoffs

This file defines local orchestration policy. It is not an official MiniMax model specification.

## Route by requested deliverable

| Requested deliverable or missing layer | Owner |
|---|---|
| Static image prompt, character sheet, portrait, location, prop, keyframe prompt, storyboard still, or image edit | Optional `$lira-image-prompts` |
| Acting master profile, fixed voice, scene performance, objective, tactic, beats, reactions, eye life, physical business, or performance repair | Optional `$acting-for-ai-video` |
| Complex blocking, gaze, camera, optics, timing, physics, lighting, dialogue/audio direction, cuts, or continuity design | Optional `$cinedance-seedance-director` as directing input |
| H3 mode selection, official Context-IR structure, reference semantics, settings separation, final H3 QA | `$minimax-h3-director` |

H3 final assembly always belongs to `$minimax-h3-director`. Never hand final ownership to a Seedance specialist.

## Select the smallest chain

- Raw H3 scene with concrete filmable behavior: assemble directly.
- Raw scene with abstract performance: ACTING, then H3.
- Requested static assets only: LIRA; do not silently add an H3 prompt.
- Static asset prompts plus eventual H3 prompt: LIRA, mark assets as planned, then block actual reference binding until assets exist unless a template was requested.
- Complex cinematic H3 shot with sufficient assets: CINEDANCE directing analysis, then H3 translation.
- Complete package: use only the specialists needed for explicitly requested artifacts, then assemble H3 last.
- Existing complete Seedance prompt: translate directly; invoke an expert only to repair a specific weak layer.

Do not invoke LIRA because a video happens to contain a person, location, or prop. Do not invoke ACTING when behavior is already concrete and no performance artifact is requested. Do not invoke CINEDANCE for a simple H3 formatting conversion with adequate directing detail.

## Resolve optional dependencies

1. Inspect the current available-skills catalog for the exact skill name.
2. If selected and available, read its entire `SKILL.md` and all references that its own routing requires.
3. If selected but unavailable, name it exactly and explain which requested layer cannot receive specialist treatment.
4. Continue only if the remaining supplied information is sufficient for a valid artifact.
5. Never search a conventional filesystem path as a substitute for catalog availability, and never recreate a missing specialist from remembered rules.

## Preserve handoffs

Treat user-provided facts, exact dialogue, visible text, asset identifiers, relationships, duration, aspect ratio, media roles, and approved creative decisions as immutable unless the user changes them.

Keep these as separate artifacts:

- Static asset prompts
- Acting master profile
- Fixed voice prompt
- Scene-adapted performance
- H3 settings
- H3 Context-IR prompt

Pass only the downstream-relevant portion. Never paste an entire acting master profile into every shot. Never expose specialist routing notes or reasoning inside the H3 prompt.

## Handle blockers visibly

- Missing actual image/video/audio: complete independent prompt or planning work, then state that reference-bound H3 assembly awaits the real asset.
- Missing exact dialogue: do not invent words. If speech is optional, omit it; if central, request the line.
- Unknown duration that changes final-frame alignment or timecodes: ask for it before claiming the prompt is production-ready.
- Input exceeds H3 limits: identify the exact excess and propose prioritization or segmentation.
- Target model is ambiguous between H3 and Seedance: ask one concise model question because it changes final ownership and syntax.

## Resolve conflicts

Official H3 syntax always overrides a specialist's output format. Specialist creative decisions may refine missing detail but may not override locked user facts. When two specialists conflict, preserve the upstream artifact that owns the fact and let H3 requirements control final representation.
