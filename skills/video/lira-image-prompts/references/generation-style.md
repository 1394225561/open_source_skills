# Lira Generation Style and Building Blocks

Read this reference for new character, scene, location, or prop generation. It owns platform parameters, technical camera and film blocks, palette construction, mood references, positive constraint patterns, and standing generation rules.

## Contents

- Platform parameters
- Technical capture blocks
- Palette and cinematographer references
- Positive constraint patterns
- Standing rules and prompt-type introduction

# Formulas & Building Blocks

Reusable components for image prompts. Keep them consistent within a project so
generated assets match each other.

## Platform parameters (set in the UI, never in prompt text)

- **Aspect ratio:** 21:9 cinemascope locations (Soul Cinema); 16:9
  character/casting sheets; 9:16 vertical/UGC; 1:1 props; 3:4 or 2:3
  portraits. Soul 2.0 has NO 21:9 — widescreen character plates go to Soul
  Cinema with a Soul ID.
- **Quality/resolution:** Soul models render 1.5k/2k; NBP, Seedream 4.5 and
  GPT Image 2 go up to 4K.
- **Soul ID:** character identity on Soul 2.0 / Soul Cinema — set in the UI,
  reinforce with consistent prose anchors (same wardrobe, same marks).
- **Cinema Studio AI Cast:** builds a character reference sheet
  AUTOMATICALLY — standalone tool on Higgsfield, all parameters set in its
  UI; no prompt needed. Offer it as the fast path when the goal is a
  reference sheet.

## Tech blocks (camera + film stock)

**Film-grain cinematic register:**
```
Photorealistic ARRI Alexa LF anamorphic Cooke S4 lens at T2.0, organic 35mm
Kodak Vision3 250D film grain, soft cinematic falloff, cinematic film still
aesthetic
```
(For this register use desaturated grading + cinematographer mood. Do NOT write
"painterly" on photoreal character sheets — it triggers illustration.)

**Modern clean digital register:**
```
Shot on ARRI Alexa Mini LF with ARRI Signature Prime lens, clean modern digital
cinematic capture, crisp natural detail, minimal fine grain, soft cinematic
falloff, modern cinematic film still quality, hyperrealistic photographic detail
```
With: `natural living skin tones, medium contrast, subtle cool tone in the
shadows, true-to-life modern colour, no heavy desaturation`. (Distinct from the
film-grain register — no heavy grain, no strong desaturation.)

Note: Soul Cinema already carries film texture and natural grain by default —
keep tech blocks shorter there: they anchor the register, they don't need to
fight the model.

## Palette wrapper

```
Refined desaturated [painterly] palette: [cool/dominant tones] dominating,
[warm element] as the only warm contrast, deep crushed blacks, restrained
naturalistic grading, soft low contrast, strong cinematic chiaroscuro
```
Drop the word "painterly" for photoreal character work. Keep it only for
intentionally painterly environment plates. Percentages read well on all
models ("60% warm ochre, 30% deep charcoal, 10% rust-red") — name real hues
in words, keep the 60/30/10 logic. Derive the 60/30/10 split from the user's
instructions, the scene context, or the references the user uploads — never
invent a palette over them.

## Cinematographer / mood references

- **Roger Deakins** — Blade Runner 2049, Jesse James, 1917 (naturalistic light)
- **Emmanuel Lubezki** — The Revenant, Tree of Life (natural light, wide)
- **Hoyte van Hoytema** — Interstellar
- **Christopher Blauvelt** — First Cow
- **Paweł Pawlikowski** — Cold War, Ida (modern melancholy in historic
  architecture — canonical for austere institutional interiors)
- **Andrei Tarkovsky** — Mirror, Stalker (frame-within-frame interior→exterior)
- **Akira Kurosawa** — quiet landscape stillness
- **Naomi Kawase** — atmospheric Japanese rural

## Negatives — positive-only approach

No model here has a negative-prompt parameter, and prose NOT-stacks inject
the very concepts they ban.

- Photoreal guard → strengthen positive anchors: film stock, lens, real
  materials, "cinematic film still" (never "painterly" / "reference sheet")
- Empty location → "empty deserted street, bare walls, still air" — state
  emptiness as a quality of the scene
- Want clean skin → write "clean dry skin" (not "no acne")
- No logos on a prop → "plain unbranded wrapper, blank matte surface" in the
  positive; never name the brand at all
- In EDIT prompts removal is a legal operation ("Remove the lamppost") —
  always paired with the fill ("continuous brick wall behind")


---

## Standing rules

- Add `rule of thirds` to every video/image prompt — EXCEPT character sheets.
- Seedance/video: describe characters already in action states, not the process
  of getting there ("states not transitions" — mid-throw, mid-punch, mid-jump;
  not "reaches into bag, pulls out, winds up").
- Don't bloat: target ≤1500–2000 chars; filler dilutes attention on every model.

---

# Prompt-Type Templates

Skeletons for each build type. Fill with the building blocks from the Formulas & Building Blocks section.
Aspect ratio and quality/resolution are platform parameters — set them in the
UI, never in the prompt text.
