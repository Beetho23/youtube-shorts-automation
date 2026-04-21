"""
Merge video clips with voice narration
"""

import os
import subprocess

VIDEO_FOLDER = "../output"
AUDIO_FOLDER = "../voice"
OUTPUT_FOLDER = "../final"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

videos = sorted(os.listdir(VIDEO_FOLDER))
audios = sorted(os.listdir(AUDIO_FOLDER))

for i in range(min(len(videos), len(audios))):

    video_path = os.path.join(VIDEO_FOLDER, videos[i])
    audio_path = os.path.join(AUDIO_FOLDER, audios[i])
    output_path = os.path.join(OUTPUT_FOLDER, f"short_{i+1}.mp4")

    subprocess.run([
        "ffmpeg",
        "-i", video_path,
        "-i", audio_path,
        "-map", "0:v",
        "-map", "1:a",
        "-shortest",
        output_path
    ])

    print(f"Merged: {output_path}")

print("All videos merged!")
