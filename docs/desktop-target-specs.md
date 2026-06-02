# Desktop Target Specifications

## Platform Scope

- Target platforms: Desktop only (Windows 10+, macOS 12+, Ubuntu 22.04+).
- Runtime mode: Offline-capable by default; no mandatory internet dependency for startup or gameplay.
- Primary orientation: Landscape.

## Display Targets

- Supported aspect ratios: 16:9 (primary), 16:10, 21:9.
- Minimum render resolution: 1280x720.
- Recommended resolution: 1920x1080.
- Maximum validated resolution: 3840x2160.
- Window modes: Windowed, borderless windowed, fullscreen exclusive (where supported).
- DPI scaling support: 100%, 125%, 150%, 200%.

## UI Layout Constraints

- Safe area margins: minimum 4% horizontal, 4% vertical.
- Base layout grid: 8 px spacing system.
- Anchor behavior:
  - Primary HUD elements anchor to corners with safe margins.
  - Center overlays remain centered with responsive max-width.
  - Dialogs use min/max width constraints and vertical scroll fallback.
- Text scaling:
  - Base UI scale: 1.0 at 1080p.
  - Scale multipliers: 0.9 (720p), 1.0 (1080p), 1.25 (1440p), 1.5 (4K).

## Input Targets

- Required input devices: Keyboard + mouse.
- Optional support: Standard gamepad (XInput/SDL compatible).
- Navigation expectations:
  - Every interactive control has visible hover/focus/active states.
  - Full keyboard navigation for menus (Tab/Shift+Tab, arrows, Enter/Escape).
  - Gamepad focus ring parity with keyboard focus.

## Minimum & Recommended Hardware

- Minimum CPU: 4 logical cores @ 2.5 GHz (2018 equivalent).
- Recommended CPU: 6+ logical cores @ 3.0 GHz (2020 equivalent).
- Minimum GPU: dedicated/integrated GPU with DX11/Metal/Vulkan support and 2 GB VRAM shared/effective.
- Recommended GPU: 4+ GB VRAM class desktop GPU.
- Minimum RAM: 8 GB.
- Recommended RAM: 16 GB.
- Storage budget target: <= 5 GB install footprint for base game package.

## Frame-Time Targets

- Target framerate: 60 FPS on recommended spec at 1080p (medium preset).
- Playable floor: 30 FPS minimum on minimum spec at 720p (low preset).
- Frame-time stability target: 95th percentile <= 22 ms in gameplay scenes.
