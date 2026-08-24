# Lira Image Editing

Read this reference for every edit of an existing frame, including NBP edits, Seedream texture repair, GPT Image 2 local surgery, and edit-lane QA. For location view changes, also read scene-location-generation.md.

## Nano Banana Pro (NBP) — edits (always first) and props

- **Role 1 — edits:** every frame edit starts on NBP; an edit =
  post-processing of the ORIGINAL (the original is the base, change the
  minimum; rebuilding a frame with an edit is forbidden — that is a
  regeneration in a Soul model).

---

## Source context: Nano Banana Pro edit continuation

- **Location view change on NBP:** you MUST force the model to understand
  the new object arrangement — spell it out explicitly: if the sofa was on
  the right in the main view, in the reverse view it must end up on the
  LEFT, and so on for every major object. Without the explicit new
  arrangement NBP scrambles the geometry.
- **Template:** the surgical edit from the Formulas & Building Blocks section — minimal CHANGE,
  exhaustive PRESERVE EXACTLY, one change per pass.

## Seedream 4.5 — texture pass ONLY

- **Its only role:** reviving sloppy AI textures in a finished frame —
  skin (pores), fabric (weave), surfaces (dirt, texture).
- **Does NOT work for point edits** — never hand it one.
- **Resolution:** basic up to 4K / high up to ~6K. Multi-reference.
- **Prompt:** goal = "reviving sloppy AI textures"; CHANGE lists the
  surfaces; PRESERVE locks composition, face, light, grade.

## GPT Image 2 — last-resort local surgery + location view changes

- **Character:** very "dirty" across the frame as a whole (touches the
  entire image), but excellent locally.
- **Role 1 — edits:** only the finest local edit of one small element,
  when NBP couldn't take it. The smaller the CHANGE, the cleaner the
  result.

---

## Source context: GPT Image 2 edit continuation

- **Resolution:** 1k / 2k / 4k; quality low / medium / high.
- **Template:** the same surgical edit; make the PRESERVE list maximally
  exhaustive, because the model happily repaints what it shouldn't.

---


---

## Surgical-edit template (NBP first — the whole edit lane uses it)

Minimal change, exhaustive preservation. This is what makes edits clean.

```
Edit the image: [one-line goal].

CHANGE: [only the single thing that changes, described precisely].

PRESERVE EXACTLY:
- [list every element that must stay identical: face, clothing, props,
  positions, wall/floor, camera angle, all existing shadows]
- Color grade, palette, contrast, grain, falloff

ONLY CHANGE: [restate the one change]. 100% identical otherwise.
```
Lesson: when the user says you overdid it or drifted from the ask, you changed
too much. Lock everything, change one thing.

**Seedream 4.5 texture pass** (its only role): goal = reviving sloppy AI
textures; CHANGE names the surfaces (skin pores, fabric weave, ground dirt);
PRESERVE locks composition, identity, light, grade. Never a point edit.

**GPT Image 2** (last resort): same template, narrowest possible CHANGE — it
dirties the frame globally, so the smaller the ask, the cleaner the result.


---

## Image edit — NBP first, always

Use the surgical-edit template in the Formulas & Building Blocks section. Minimal CHANGE, exhaustive
PRESERVE EXACTLY. One change at a time. Lock face, wardrobe, props, camera,
shadows, and grade unless explicitly changing them. The edit is
post-processing of the ORIGINAL — never a rebuild of the frame.

- Any edit starts on **NBP**.
- Sloppy AI textures (skin, fabric, surfaces) → **Seedream 4.5 texture
  pass** — its only role; never point edits there.
- Finest local micro-edit NBP couldn't take → **GPT Image 2**, last resort:
  dirty globally, strong locally — keep the CHANGE as small as possible.
- Frame needs rebuilding → not an edit; regenerate in a Soul model.
