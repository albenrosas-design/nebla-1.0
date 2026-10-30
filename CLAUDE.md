# nebla-1.0

Marketing workspace for Dr. Alben Rosas (dralbenrosas.com). Brand data: `brand-profile.json`.

## Video toolchain

- Skills in `.claude/skills/`: `video-use` (main editor), `remotion-*` (alt engine). Versions in `skills-lock.json`.
- HyperFrames (motion graphics) comes from the `hyperframes@hyperframes` plugin, enabled in `.claude/settings.json`.
- Default deliverable: vertical 9:16, 1080x1920, for TikTok / Reels / Shorts. Landscape sources need a crop to 9:16 (render.py only scales).
- Remotion project: `videos/`.
- New session: run `scripts/setup-video-tools.sh` and `export` the lines it prints.
- yt-dlp lives in `~/.local/bin`; TikTok/Instagram are blocked by the cloud proxy, so downloads only work locally.
- video-use needs `ELEVENLABS_API_KEY` (env var or `.claude/skills/video-use/.env`, git-ignored, never committed).
- api.elevenlabs.io must be in the cloud environment's allowed domains, or transcription fails.
