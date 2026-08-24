# Lira Scene and Location Generation

Read this reference for locations, environments, cinematic stills, establishing frames, Soul Cinema, reverse angles, or another camera position in the same location.

## Higgsfield Soul Cinema — locations and cinematic frames

- **Specialty:** cinema-grade stills, concept art, establishing shots,
  film stills.
- **Quality:** 1.5k / 2k. **Aspects:** 1:1, 4:3, 3:4, 16:9, 9:16, 3:2,
  2:3, **21:9 available** — cinemascope plates go here.
- **Reference:** 1 image; a Soul ID character can be placed into a
  cinematic scene.
- **Strengths:** film textures, natural grain, light/shadow work,
  era-specific aesthetics, skin and fabric.
- **Performs best on:** close-ups and mood-driven scenes; frames work
  great as keyframes for video generation.
- **Don't over-stack grain/film words** — the model carries them natively:
  one register line from the tech block is enough.
- **Camera anchor** — the main pain point of locations: simple wording
  ("high angle three-quarter wide shot, camera high above the room looking
  diagonally down at 45 degrees") beats abstract jargon (CCTV/fisheye).


---

## Source context: GPT Image 2 location-view role

- **Role 3 — location view change:** a reverse angle / another angle of
  the same location works well on GPT Image 2 — route this task here.

---

## Location / environment — Soul Cinema

Platform parameters: aspect 21:9 for cinemascope plates (16:9 if the shot is
for standard video), quality 2k.

```
[Camera anchor — the hardest part; anchor it hard]. [Location identity].
[Key architectural / natural elements]. [Light source + direction + temperature].
[Secondary elements receding into depth]. [Palette wrapper]. [Tech block].
[Mood / cinematographer ref]. [Emptiness stated positively if the location
must be empty: "empty deserted interior, bare walls, still air"].
```

Camera-anchor tips (the recurring pain point):
- Simple beats abstract: `high angle three-quarter wide shot, camera high above
  the room looking diagonally down at a 45 degree angle` works; CCTV/fisheye/
  extreme-corner jargon often fails or over-distorts.
- Use real-world equipment + genre terms (24mm wide, real estate interior photo)
  over abstract geometry.
- For floor/plank direction and other stubborn geometry, anchor it in the
  positive description and reframe ("horizontal stripe pattern, no vanishing
  point in the floor" instead of fighting "planks").
- Frame-within-frame (interior→exterior through a doorway/window): foreground
  ruin walls as dark silhouettes around the opening; Tarkovsky Stalker mood.
- Optics/DOF language stays OFF locations — it belongs to characters.
- Soul Cinema carries film grain and texture natively — don't over-stack grain
  words; one register line from the tech block is enough.


---

## Source context: Location view-change workflow

**View change of a location (reverse angle / new camera position):**
- **GPT Image 2** handles location view changes well — default route.
- On **NBP** you must FORCE the model to understand the new object
  arrangement — spell out the mirrored blocking explicitly, object by
  object: "In the main view the sofa is on the right; in this reverse view
  the sofa is on the LEFT, the doorway behind the camera is now visible
  ahead". Anchor every major object's new position; without it NBP scrambles
  the geometry.
