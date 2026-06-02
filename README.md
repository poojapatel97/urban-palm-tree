# urban-palm-tree

Dragon and avatars game implementation.

## Run

```bash
python dragon_and_avatars_game.py
```

Input format:

1. `dragon_health dragon_attack`
2. `number_of_avatars`
3. `avatar_health avatar_attack` (repeated for each avatar)

Output:

- `DRAGON` if the dragon defeats all avatars
- `AVATARS` otherwise
Desktop/offline game delivery baseline focused on clear UI, stable graphics, and glitch prevention.

## Implementation Artifacts

- `docs/desktop-target-specs.md` — desktop hardware, display, and input constraints.
- `docs/offline-first-architecture.md` — offline runtime guarantees, local state/storage model, and startup behavior.
- `docs/ui-style-guide.md` — visual token system, layout rules, HUD patterns, and accessibility clarity standards.
- `docs/ui-clarity-and-glitch-controls.md` — concrete controls for readability, scene safety, frame pacing, and failure handling.
- `config/graphics-quality-matrix.json` — deterministic low/medium/high graphics presets with default tier mapping.
- `qa/desktop-validation-checklist.md` — desktop validation matrix and release-gate checklist.
