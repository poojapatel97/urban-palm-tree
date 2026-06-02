# Offline-First Architecture

## Core Requirement

All core gameplay, rendering, and settings management must function without network access.

## Runtime Guarantees

- No required remote API calls in bootstrap path.
- No blocking network checks during startup.
- All runtime-critical assets are packaged locally with the application build.
- Save/load, settings, and progression operate entirely via local storage.

## Asset Strategy

- Bundle all mandatory assets into versioned local packs.
- Use deterministic asset manifests:
  - Asset ID
  - Local path
  - Hash/checksum
  - Fallback reference
- Preload startup-critical assets before first interactive frame.
- On missing/corrupt asset:
  - Log structured error locally.
  - Load fallback asset.
  - Keep session alive unless fallback is unavailable and asset is critical.

## Local Persistence Model

- Persist data under app-specific local data directory per OS.
- Store:
  - User settings (video/audio/input/UI scale)
  - Save-state/progression
  - Local diagnostics snapshots (bounded ring buffer)
- Requirements:
  - Atomic writes for save files.
  - Backup slot for last known-good state.
  - Versioned schema with migration path.

## Startup Flow (Offline-Safe)

1. Initialize logging and local storage.
2. Validate settings schema and migrate if needed.
3. Validate local asset manifest integrity.
4. Load startup scene essentials from local bundles.
5. Enter main menu without any network dependency.

## Optional Online Features (Non-Blocking)

- Optional services (leaderboards/cloud sync/news) must:
  - Be disabled by default in offline mode.
  - Run asynchronously after core startup.
  - Never block rendering, input, or save/load.

## Failure Handling

- Recoverable failures:
  - Missing optional assets/services -> fallback + warning.
  - Local save parse error -> revert to backup slot + user notice.
- Non-recoverable failures:
  - Critical bootstrap asset absent and no fallback -> fail fast with explicit error screen.
