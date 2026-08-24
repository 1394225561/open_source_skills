---
name: cinedance-seedance-director
description: Convert a scene, shot brief, storyboard beat, reference set, or existing prompt into a production-ready cinematic Seedance 2.0 or Higgsfield Seedance video prompt. Use when directing or fixing first-frame occupancy, reference tags, spatial blocking, gaze, body orientation, landmark proximity, single-take or multi-shot structure, optics, camera movement, physical motion, lighting, timing, dialogue, audio, continuity, or context leakage.
---

# Cinedance Seedance Director

Always read [references/core-workflow.md](references/core-workflow.md). Classify the task, then completely read the union of applicable references:

- **Complete shot/rewrite:** [spatial-and-references.md](references/spatial-and-references.md), [camera-and-optics.md](references/camera-and-optics.md), and [motion-physics-lighting.md](references/motion-physics-lighting.md).
- **Subjects, tags, geography, first frame, blocking, gaze, orientation, landmarks:** [spatial-and-references.md](references/spatial-and-references.md).
- **Lens, FOV, focus, framing, camera, composition, handheld:** [camera-and-optics.md](references/camera-and-optics.md); also load spatial rules when framing affects placement, direction, gaze, or landmarks.
- **Action, timing, contact, materials, physics, light, exposure:** [motion-physics-lighting.md](references/motion-physics-lighting.md).
- **Speech, narration, offscreen/prior audio, lip-sync, deliberate silence/mix:** [dialogue-and-audio.md](references/dialogue-and-audio.md).
- **Multiple shots, cuts, montage, or cross-cut continuity:** [multi-shot-continuity.md](references/multi-shot-continuity.md) plus camera-and-optics.
- **Comprehensive audit:** all references.

Apply the selected rules as one director system and run the core silent QA. Unless the user explicitly asks for analysis, variants, critique, or explanation, return only the final cinematic English Seedance prompt in the prescribed structure.
