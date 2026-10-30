#!/usr/bin/env bash
# Installs the runtime deps for the video toolchain (video-use, HyperFrames, Remotion, yt-dlp).
# Skills themselves live in .claude/skills/ and are versioned in skills-lock.json.
set -euo pipefail

command -v ffmpeg >/dev/null || { echo "ffmpeg missing: brew install ffmpeg | sudo apt-get install -y ffmpeg"; exit 1; }

# video-use helpers + yt-dlp (curl-cffi enables TikTok/Instagram impersonation)
python3 -m pip install -q --user requests librosa matplotlib pillow numpy "yt-dlp[default,curl-cffi]"

# Remotion project
(cd "$(dirname "$0")/../videos" && npm i --silent)

# Cloud sessions can't download Chrome; reuse the preinstalled one when available.
if [ -x /opt/pw-browsers/chromium ]; then
  echo "export REMOTION_BROWSER_EXECUTABLE=/opt/pw-browsers/chromium"
  echo "export HYPERFRAMES_BROWSER_PATH=$(ls -d /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell | head -1)"
fi

[ -n "${ELEVENLABS_API_KEY:-}" ] || grep -qs '^ELEVENLABS_API_KEY=..' .claude/skills/video-use/.env \
  || echo "NOTE: set ELEVENLABS_API_KEY (needed by video-use for transcription)"
echo "video tools ready"
