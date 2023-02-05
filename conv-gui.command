#!/usr/bin/env python3

command -v ffmpeg >/dev/null 2>&1 || command -v avconv >/dev/null 2>&1 || { echo >&2 "Error: ffmpeg or avconv is required but not found. Please install it and try again."; exit 1; }

python3 conv-gui.py