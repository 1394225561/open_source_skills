# H3 Model Capabilities

> **MODIFIED FILE NOTICE:** This operational reference was created by adapting MiniMax-AI/MiniMax-H3 `README.md`, `README.zh-CN.md`, and reproducible request scripts. It is not an unmodified official file.

Source basis: MiniMax-AI/MiniMax-H3 at commit `6da473b48daf91e5aebfb56451f8a0b116348df5` (2026-08-13). See the bundled `LICENSE` and `NOTICE` files. This is a concise operational adaptation, not a complete mirror of the repository.

## Official model facts

- Output duration is 4-15 seconds per generation.
- Common supported aspect ratios include 21:9, 16:9, 4:3, 1:1, 3:4, and 9:16; support is not limited to this example list.
- The default H3-Base output has a 768-pixel short edge.
- A 2K result is produced through the separate H3-Regenerate-2K stage; do not describe ordinary H3-Base generation as native 2K output.
- Output is 24 FPS with native 32 kHz stereo audio.
- Dialogue is stably supported in Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, and Spanish. Other languages may have varying support.

## Model families and input ceilings

H3-Base-FL2VA accepts:

- Zero images for T2VA.
- One image as either a first-frame or last-frame condition.
- Two images as first-frame and last-frame conditions.

H3-Base-Ref2VA accepts:

- Up to 9 images.
- Up to 3 video clips, each 2-15 seconds, with no more than 15 seconds of video input in total.
- Up to 3 audio clips, each 2-15 seconds, with no more than 15 seconds of audio input in total.
- Up to 12 files across all media types.
- Audio only when at least one image or video is also supplied; audio cannot be the sole media input.

## Interpret limits correctly

Treat these values as official model ceilings. A MiniMax Design, Playground, API, or local runtime may currently expose fewer choices. Apply the narrower verified interface limit for execution without rewriting it as a model limitation.

Do not infer unlisted defaults from repository examples. Sample values such as `duration_seconds: 10`, `aspect_ratio: auto`, or `seed: 0` demonstrate request shape, not mandatory defaults.

## Keep runtime configuration separate

Official reproducible H3-Base scripts separate these request properties:

```json
{
  "task": "t2va | fl2va | ref2va",
  "prompt": "expanded H3 Context-IR",
  "conditions": [],
  "target": {
    "short_edge": 768,
    "aspect_ratio": "confirmed value",
    "duration_seconds": 10
  },
  "seed": 0
}
```

Use this only as a conceptual boundary. Emit request JSON only when the user asks for it and all values and condition roles are known.

## Feasibility checks

- Reject a claimed single generation outside 4-15 seconds. For a longer work, design multiple clips with explicit start/end state handoffs.
- Count real files, not the number of semantic subjects derived from them.
- Validate video and audio clip duration individually and in aggregate.
- Distinguish 768-base generation from later 2K regeneration.
- Do not promise stable dialogue for a language outside the official eleven; describe support as variable.
