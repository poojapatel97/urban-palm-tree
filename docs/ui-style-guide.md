# UI Style Guide

## Design Goals

- Clear at a glance in gameplay and menus.
- Consistent hierarchy across all screens.
- Legible under varied resolutions and DPI scales.
- Minimal ambiguity in interaction and status feedback.

## Color System

- Primary background: `#101820`
- Surface background: `#1B2630`
- Surface raised: `#243241`
- Primary accent: `#4DB6FF`
- Secondary accent: `#7CFFB2`
- Warning: `#FFB84D`
- Error: `#FF5C7A`
- Text primary: `#F2F6FA`
- Text secondary: `#B6C2CF`

### Contrast Rules

- Body text contrast: >= 4.5:1 against background.
- Large text and icons: >= 3:1.
- Critical warning/error text: >= 7:1 preferred.

## Typography

- Font family: one sans-serif UI family with full Latin coverage.
- Scale:
  - H1: 40/48
  - H2: 32/40
  - H3: 24/32
  - Body: 18/26
  - Caption: 14/20
- Minimum readable size:
  - Body: 16 px at 1080p equivalent.
  - Caption: 13 px at 1080p equivalent.

## Spacing and Layout

- Spacing unit: 8 px.
- Component paddings: 8/12/16/24/32 (multiples of 8).
- Screen max content width:
  - Menus: 1280 px.
  - Modal/dialog: 720 px.
- Use responsive scaling while preserving minimum control sizes.

## Component States

Each interactive component must expose:

- Default
- Hover
- Focus (keyboard/gamepad)
- Active/Pressed
- Disabled
- Error (for inputs where applicable)

Focus indicators:

- 2 px minimum outline.
- Color distinct from hover.
- Visible on dark and bright backgrounds.

## Iconography

- Single icon style family (stroke or filled, not mixed in same context).
- Base icon size: 20 px with 16/24 px variants.
- Icons must include text labels for ambiguous actions.

## HUD Patterns

- Top-left: mission/context.
- Top-right: score/resources/status.
- Bottom-center or corners: ability/action bar.
- Notification stack: top-center or top-right with bounded height and timed decay.

Rules:

- Keep persistent HUD opacity below intrusive threshold in active gameplay.
- Avoid placing permanent UI over reticle/primary interaction zone.
- Use motion sparingly and consistently for attention cues.

## Screen Consistency

Apply same token system across:

- Splash/loading
- Main menu
- Settings
- Pause
- HUD
- Inventory/map/dialog overlays
- Error/recovery screens
