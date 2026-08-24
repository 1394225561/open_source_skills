# Lira Prop Generation

Read this reference for prop sheets, product-style objects, exact in-frame text on objects, or realistic NBP/GPT Image 2 object generation.

## Source context: Nano Banana Pro prop capabilities

- **Role 2 — props:** generation of prop sheets and product-style objects
  (together with GPT Image 2) — realistic product context.
- **Resolution:** 1k / 2k / 4k. **Aspects:** all standard + 21:9 and
  4:5/5:4.
- **References:** up to 14 images.
- **Conversational editing:** understands natural instructions; adjusts
  lighting and reflections to the change on its own.
- **Best in-frame text rendering:** exact copy in quotes + font/weight/color
  ("Write 'GENUINE' in bold red serif on the sign").

---

## Source context: GPT Image 2 prop capabilities

- **Role 2 — props:** product-style generation together with NBP
  (realistic product context, strong typography).

---

## Prop sheet — NBP / GPT Image 2

Props render more realistically in NBP / GPT Image 2 (strong realistic
product context + exact text on objects) — this is the one generation task
that does NOT go to a Soul model.

Platform parameters: aspect 1:1 (3:4 for tall props), resolution 2k–4k.

```
Photorealistic [top-down / three-quarter overhead] product shot of [prop] on a
[neutral grey concrete] surface, [soft directional lighting], isolated subject.
[Concrete description of the prop, materials, wear state]. [Blank unbranded
surfaces stated positively if no text/logos wanted]. [Tech block].
```

- Multiple states (clean / damaged / bloodied) = separate assets.
- Trigger-word caution: device props can hit safety flags. Describe by neutral
  materials and function ("retro industrial electronic prop assembly, numerical
  readout") rather than weapon/explosive terms.
- For "no logos": remove brand names everywhere and state "plain unbranded
  wrapper, blank matte surface" in the positive.
