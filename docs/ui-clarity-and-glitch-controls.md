# UI Clarity and Glitch-Prevention Controls

## UI Clarity Pass

- Enforce typography minimums from style guide at each supported resolution/DPI tier.
- Validate all text wrapping/clamping in:
  - Settings labels
  - Tooltips
  - Dialog titles and body copy
  - Notification toasts
- Ensure consistent visual hierarchy:
  - One primary action per view.
  - Secondary actions visually subordinate.
- Verify visible state changes on every interactive element:
  - Hover/focus/pressed/disabled.
- Ensure overlays maintain readability over dynamic backgrounds:
  - Backplates, scrims, or adaptive text shadow where required.

## Rendering Stability Controls

- Frame pacing:
  - Use fixed present strategy with optional VSync.
  - Clamp frame delta to avoid simulation spikes after stalls.
- Asset preloading:
  - Preload startup scene package and frequently used UI atlases.
  - Keep asynchronous preload queue for next-scene critical assets.
- Fallback resources:
  - Missing texture -> neutral fallback texture.
  - Missing font glyph -> fallback font family.
  - Missing icon/sprite -> placeholder with log warning.

## Scene and State Transition Safety

- Use explicit transition states:
  - Entering
  - Active
  - Exiting
- Block duplicate scene transition triggers until current transition completes.
- Guard all scene exit/enter paths against null references and race conditions.
- Persist important UI state (selected tab/focus target) across pause/resume when appropriate.

## Defensive Error Handling

- Wrap rendering/UI update loops with targeted error boundaries where engine permits.
- Log structured local diagnostics for:
  - Asset load failures
  - Scene transition failures
  - UI binding/state desynchronization
- Degrade gracefully:
  - Hide broken non-critical widgets with fallback notice.
  - Keep gameplay session running when safe.
