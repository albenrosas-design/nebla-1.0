# nebla-1.0

Marketing workspace for Dr. Alben Rosas (dralbenrosas.com). Brand data: `brand-profile.json`.

## Video toolchain

- Skills in `.claude/skills/`: `video-use` (main editor), `hyperframes*` + `media-use` (motion graphics), `remotion-*` (alt engine). Versions in `skills-lock.json`.
- Remotion project: `videos/`.
- New session: run `scripts/setup-video-tools.sh` and `export` the lines it prints.
- yt-dlp lives in `~/.local/bin`; TikTok/Instagram are blocked by the cloud proxy, so downloads only work locally.
- video-use needs `ELEVENLABS_API_KEY` (env var or `.claude/skills/video-use/.env`, never committed).
