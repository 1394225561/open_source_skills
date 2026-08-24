# Seedance to H3 Adaptation

This file defines a translation procedure. It does not make Seedance syntax valid in H3.

## Translate intent, not surface format

1. Extract immutable user facts, active real assets, dialogue, visible text, shot duration, aspect ratio, and approved creative decisions.
2. Extract transferable directing intent: first-frame occupancy, blocking, gaze, body orientation, camera, focus, lighting, physical contacts, timing, dialogue delivery, sound, and continuity.
3. Remove Seedance platform concepts and classify the actual H3 inputs.
4. Select the H3 prompt mode and runtime task by actual input role.
5. Re-encode the retained content in the official H3 Base or Ref2VA structure.

## Remove or remap Seedance-only elements

- Remove `Seedance`, `Higgsfield`, `R2V`, `T2V`, `Soul ID`, platform UI steps, and model-selection prose from the final prompt.
- Do not carry `@TAG` syntax unless the exact supplied H3 interface genuinely uses that handle. For Ref2VA, map real assets into the official label system.
- Replace Seedance section headings, lens-lock boilerplate, diagonal-FOV blocks, and repeated negative lists with observable shot content inside the appropriate H3 field.
- Replace Seedance timing ranges with H3 shot numbering and cut-time notation. Shot 1 has no timestamp; later shots use exact cut times.
- Preserve dialogue verbatim but encode it through stable `(Sx)` IDs and `<d>[Language] ...</d>`.
- Preserve useful first-frame and continuity constraints, but use the exact Base alignment instruction only when the image is a real I2VA/FL2VA/L2VA condition.

## Do not fabricate reference conversions

A Seedance `@TAG` with no corresponding real H3 asset cannot become `<Picture N>`, `<Video N>`, `<Audio N>`, or an active `<Subject N>`. Keep the descriptive identity information if useful, omit the false binding, and report the missing asset when fidelity depends on it.

A text-only Seedance prompt is source text, not Ref2VA media. Use T2VA unless real keyframes or multimodal references are also supplied.

## Preserve cinematic control selectively

Keep:

- Visible subject position, scale, orientation, gaze, and landmark relationships
- Filmable action, reaction, contact, inertia, and consequence
- Camera shot size, height, angle, movement, focus, perspective, and composition result
- Lighting direction and state continuity
- Exact dialogue, voice behavior, diegetic sound, ambience, and score intent
- Cross-shot identity, geography, screen direction, object state, damage, and emotional progression

Discard:

- Unsupported lens metadata presented as mandatory model syntax
- Generic quality adjectives and duplicated constraints
- Planning notes, prior-scene residue, unused characters, and unused references
- Seedance-specific output wrappers and submission instructions

## Verify the conversion

- No stale Seedance or Higgsfield platform syntax remains.
- The H3 mode reflects real inputs rather than the source prompt's former mode name.
- Base and Ref2VA structures are never mixed.
- Every reference label has a real source asset.
- Dialogue and visible text retain their original language while the descriptive body is English.
- Runtime settings remain outside the H3 prompt.
