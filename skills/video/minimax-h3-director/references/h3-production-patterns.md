# H3 Production Patterns

> **MODIFIED FILE NOTICE:** This local production reference adapts selected patterns from MiniMax-AI/MiniMax-H3 style-specific skills and adds local orchestration policy. It is not an unmodified official file.

Source basis: transferable patterns observed in the eight style-specific skills bundled with MiniMax-AI/MiniMax-H3 at commit `6da473b48daf91e5aebfb56451f8a0b116348df5`, plus local cinematic orchestration policy. See the bundled `LICENSE` and `NOTICE` files. Those style skills declare MiniMax Hub dependencies and are not runtime dependencies of this skill.

## Authority boundary

Use these as production heuristics, not H3 model facts. Do not copy Hub canvas operations, choice-card requirements, `hub_generate_*` calls, fixed visual styles, pricing claims, or Seedance fallback logic.

## Plan around verified inputs

- Route by the artifact the user needs now, not by nouns incidentally present in the brief.
- Record the role and provenance of every critical asset before binding references.
- Treat the latest explicitly approved asset or decision as authoritative.
- Separate character, scene, style, text, action, camera, audio, and temporal-reference roles.
- Confirm or request only decisions that change mode, feasibility, reference binding, or locked output.

## Keep shots feasible

- Fit every shot and spoken line inside the confirmed duration.
- Give each beat one primary action and enough time for setup, action, consequence, and reaction.
- Prefer one continuous shot for first-to-last-frame interpolation.
- Use cuts only when they add new information; preserve identity, geography, screen direction, light, object state, damage, and emotional progression across them.
- For work longer than 15 seconds, create independent H3 clips with explicit outgoing and incoming state locks.

## Preserve asset truth

- Use official, user-supplied, licensed, or otherwise verified assets for exact identities, products, logos, interfaces, and claims.
- Never polish or strengthen an invented substitute as though it were authentic.
- Keep prompt-prepared assets separate from generated assets.
- Strip planning labels and storyboard annotations that should not appear in the target video.

## Design audio with the picture

- Allocate dialogue, vocal delivery, ambience, physical effects, diegetic music, and non-diegetic score deliberately.
- Preserve speaker identity and audio continuity across cuts.
- Avoid duplicating the same soundtrack as both native generated audio and a separately reused track.
- Make silence explicit only when requested; otherwise describe the intended natural sound field.

## Recover from weak generations

When a result drifts or becomes incoherent:

1. Identify the failed layer: identity, reference role, blocking, action complexity, timing, camera, text, audio, or continuity.
2. Strengthen the exact active reference anchor and the visible target state.
3. Remove competing actions, unused references, and generic constraints.
4. Simplify the camera or shorten the action.
5. Split an overloaded shot into multiple H3 generations when needed.
6. Preserve successful states and change only the failed layer in the next prompt.

Do not respond to failure by adding an indiscriminate negative-prompt wall.

## Final production QA

- Every requested artifact exists or is explicitly marked blocked/planned.
- Every factual claim and exact asset has traceable provenance.
- The H3 prompt contains only generation-relevant content.
- Shot duration, dialogue timing, action load, and transitions are physically plausible.
- First and last states are explicit where continuity or keyframes require them.
- Audio sources and reuse/reference relationships are unambiguous.
