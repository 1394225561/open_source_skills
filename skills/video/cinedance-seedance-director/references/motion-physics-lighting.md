# CINEDANCE Motion, Physics, and Lighting

Read this reference whenever a request creates, changes, or audits physical action, material behavior, movement timing, exposure, light direction, or lighting preservation.

## Contents

- Physics and material behavior
- Lighting priority and direction
- Action timing

## Physics lock

Every object and body has physical properties.

Enforce:

- gravity
- mass
- inertia
- friction
- contact
- weight transfer
- ground pressure
- collision
- follow-through
- cloth delay
- hair delay
- liquid flow
- blood viscosity
- snow accumulation
- fire heat shimmer
- vehicle mass
- door hinge resistance
- weapon weight

Motion must have cause and effect.

No floating bodies.

No weightless weapons.

No frictionless feet.

No teleporting.

No impossible object movement.

No rubbery CG motion.

No fake game-engine physics.

For walking:

- heel contact
- weight transfer
- hip shift
- toe push-off
- body mass settling

For running:

- real ground contact
- knee lift
- opposing arm swing
- torso lean
- varied stride
- no floaty CG-running look

For weapons:

- arm carries visible weight
- wrist angle reacts to mass
- object has inertia
- motion has acceleration and deceleration
- blade or object does not teleport between poses

For liquids:

- blood clings, drips, smears, pools, stains, and follows gravity
- droplets travel in parabolic arcs
- wet contact leaves visible residue
- flow has viscosity and direction

For snow, smoke, fire, dust, particles:

- particles move with wind direction
- particles exist in foreground, midground, and background if atmosphere is critical
- objects accumulate particles over time
- heat creates shimmer when hot air meets cold air

## Lighting priority lock

Lighting is not style decoration. It is a priority constraint.

If the shot requires backlit contre-jour, write:

```text
Subject stays between camera and the brighter background.
Camera stays on the shadow side of the subject.
Faces remain in deep shadow unless explicitly lit.
Only rim light, edge light, wet speculars, eye glints, and environmental bounce reveal detail.
No frontal key.
No flat exposure.
No beauty fill.
No studio light unless requested.
```

If previous generations became flat, strengthen:

```text
The entire shot is exposed for the backlight, not for the face.
The face is allowed to fall into crushed shadow.
The silhouette and rim contour carry the image.
```

## Lighting direction

Always define:

- primary light source
- light direction
- camera side relative to light
- subject side in shadow or rim
- background brightness
- exposure priority
- allowed highlights
- forbidden lighting failure

Example:

```text
The camera stays on the shadow side of @HERO4. Morning sun comes from camera-right, behind and to the side of him, creating gold rim light along his shoulders and head while his camera-facing back stays dark. No flat front light, no beauty fill.
```

## Action timing

For timed shots, write events in time blocks.

Use:

```text
0:00 to 0:03
0:03 to 0:06
0:06 to 0:09
0:09 to 0:12
```

Each time block should include:

- subject position
- action
- camera behavior
- critical prop state
- physics
- audio if relevant

Do not overload one time block with contradictory actions.

For single continuous takes, ensure the action can physically happen in the available time.

For multi-shot sequences, every cut must have a reason.
