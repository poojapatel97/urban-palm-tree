# Desktop Validation & Release Gate Checklist

## Environment Matrix

- [ ] 1280x720 windowed (100% DPI)
- [ ] 1920x1080 fullscreen (100% DPI)
- [ ] 2560x1440 windowed (125% DPI)
- [ ] 3840x2160 fullscreen (150% or 200% DPI)
- [ ] 16:10 aspect ratio validation
- [ ] 21:9 aspect ratio validation

## Input Validation

- [ ] Keyboard-only menu navigation works end-to-end.
- [ ] Mouse hover/click states are consistent on all primary screens.
- [ ] Gamepad focus navigation parity with keyboard/menu controls.
- [ ] Input prompts update correctly when switching devices.

## UI Readability & Layout

- [ ] No text clipping, overlap, or truncation in core screens.
- [ ] Contrast meets style guide thresholds for all major UI text.
- [ ] Focus indicators are always visible and unambiguous.
- [ ] HUD elements stay inside safe area across all supported resolutions.
- [ ] Overlay readability remains clear over bright/dark gameplay scenes.

## Graphics & Performance

- [ ] Low preset selected by default on minimum-tier hardware.
- [ ] Medium preset selected by default on recommended-tier hardware.
- [ ] High preset selected by default on high-end hardware.
- [ ] 60 FPS target reached on recommended hardware at 1080p medium.
- [ ] No severe frame-time spikes during scene transitions/loading.

## Offline Runtime Validation

- [ ] Application boots fully with network disconnected.
- [ ] Core gameplay loop works without internet access.
- [ ] Save/load works offline and survives restart.
- [ ] Optional online features fail gracefully and do not block gameplay.

## Glitch/Defect Sweep

- [ ] No flickering UI panels, z-fighting, or persistent artifacting.
- [ ] No transient null-state UI (empty widgets, broken bindings).
- [ ] No animation/state desync after pause/resume or scene changes.
- [ ] Missing asset paths show fallback resources instead of crashes.

## Smoke Test Scenarios

- [ ] Fresh install -> first launch -> main menu.
- [ ] New game start -> gameplay -> pause -> resume.
- [ ] Change graphics preset -> apply -> restart -> settings persist.
- [ ] Trigger controlled asset fallback path and confirm graceful behavior.
- [ ] Load existing save -> continue gameplay -> save again.

## Release Gate

- [ ] No major UI/graphics defects remain open.
- [ ] All critical/high-severity rendering and UX bugs are resolved.
- [ ] Known minor issues documented with acceptable risk rationale.
- [ ] Final sign-off recorded by engineering + design QA reviewers.
