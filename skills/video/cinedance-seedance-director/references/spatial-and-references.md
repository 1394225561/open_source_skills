# CINEDANCE Spatial and Reference Control

Read this reference whenever a request creates, changes, or audits subjects, reference tags, location geography, first-frame occupancy, blocking, gaze, orientation, or landmark proximity.

## Contents

- Active references and character descriptions
- Location mapping
- First-frame and spatial locks
- Gaze, orientation, and landmark locks
- Reference hierarchy

## Active references

List only active @tags used in this shot.

@tags are platform-native reference handles. They are allowed and useful when they refer to current uploaded references.

Keep active @tags exactly as provided.

Never invent new @tags.

Never include stale @tags from previous shots.

Never include a tagged character who is not visible or required in this shot.

Every @tag in the final prompt must correspond to a visible or required reference in the current shot.

## Character description rule

Describe each referenced character with only the minimum critical anchors needed for this shot.

Always include:

- age
- role or body type
- current state
- unique visible identifiers
- action-critical body parts or props
- voice only if dialogue exists
- 100% matches the reference

Do not include:

- full facial anatomy
- excessive costume detail already clear in the reference
- random adjectives
- old injuries not relevant to this shot
- props not visible or used
- relationship labels that do not affect the frame

Formula:

```text
@TAG: age + role/body type + current state + critical visible anchors + action-critical prop/body state. 100% matches the reference.
```

Example:

```text
@HERO1V2: 20yo broad-shouldered wounded male, tangled blond hair falling over his eyes, blood-streaked grey hoodie, right shoulder roughly bandaged, left hand gripping a dented steel pipe. 100% matches the reference.
```

Example:

```text
@HERO2: 25yo lean male lookout, raw emotional state, short dreadlocks tied back, cracked ski goggles pushed up on his forehead, worn olive field jacket. 100% matches the reference.
```

Reference image is the source of truth for face, body, proportions, costume, texture, and identity.

Do not overwrite the reference with excessive prose.

## Location map

If a location reference exists, convert it into a practical map before writing blocking.

Define:

- camera position
- camera facing direction
- foreground
- midground
- background
- main landmark positions
- character positions
- movement path
- lighting direction
- depth relationships

If the user says the location image is a reference, use it for:

- geography
- materials
- atmosphere
- landmarks
- lighting direction if relevant

Do not blindly inherit the camera angle, framing, or composition unless the user explicitly asks.

## First-frame occupancy lock

If the shot must start with characters visible, state it directly.

Use:

```text
The first visible frame already contains all required characters in their correct positions.
No empty establishing frame.
No delayed character reveal.
No opening frame without the required subjects.
The spatial relationship is readable immediately in frame one.
```

Only allow an empty opening if the user explicitly requests it.

If the user requests a flash cut or very short establishing cut, it must still contain the required subject or location information immediately.

No empty flash cuts.

No abstract filler.

No random landscape insert unless requested.

No first flash cut without the characters if the purpose is spatial anchoring.

## Spatial blocking lock

Always define where everyone is.

For each important subject, specify:

- screen position
- world position
- distance from landmark or other character
- body facing direction
- gaze direction
- movement direction
- foreground, midground, or background

Use simple physical language.

Example:

```text
@HERO1V2 stands within 1 meter of the burned-out car, one hand resting on the scorched hood.
@HERO2 and @HERO3 stand together in the foreground, facing @HERO1V2.
Hero2 is camera-right of the pair.
Hero3 is camera-left of the pair.
Both bodies face Hero1.
Both gaze lines are locked on Hero1.
Hero1 faces them from the car.
```

Never rely on weak words when spatial accuracy matters:

- near
- around
- beside
- somewhere
- in the area
- nearby

Replace them with:

- within 1 meter
- touching
- boots inside the root circle
- hand on the handle
- standing directly under the sign
- back against the wall
- in front of the rear passenger door
- at the south kerb edge

## Gaze line and body orientation lock

Body direction and eye direction are separate.

Always write both when character relationships matter.

Use:

- torso faces X
- eyes stay locked on X
- head turns toward X
- back faces camera
- profile faces screen-left
- character looks past camera toward X
- character does not look away unless specified

For dialogue scenes:

The speaking character’s lips move only for the scripted line.

Other characters listen silently unless explicitly speaking.

No offscreen voices unless specified.

## Landmark proximity lock

If a character must be near a landmark, anchor them physically.

Use:

- within 1 meter
- touching
- boots planted inside the root circle
- back against the wall
- hand on the door handle
- standing directly under the sign
- in front of the taxi rear door
- at the south kerb edge

Weak:

```text
near the tree
by the taxi
around the location
somewhere in the battlefield
```

Strong:

```text
@HERO1V2 stands within 1 meter of the burned-out car, one hand planted on the scorched hood.
```


---

## Reference control

Use references with hierarchy.

Identity reference controls:

- face
- body
- age
- proportions
- costume
- unique anchors

Location reference controls:

- architecture
- materials
- geography
- atmosphere
- landmarks
- lighting direction if relevant

Prop reference controls:

- shape
- scale
- material
- hand contact
- state

Vehicle reference controls:

- model
- decals
- plate
- doors
- position
- movement
- damage
- reflections

Never let a location reference override required camera angle unless requested.

Never let style references override identity, spatial blocking, action, optics, or lighting.
