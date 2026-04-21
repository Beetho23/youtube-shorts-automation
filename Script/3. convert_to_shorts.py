"""
Convert videos to vertical format (9:16) for YouTube Shorts
"""

import os
import subprocess

INPUT_FOLDER = "../final"
OUTPUT_FOLDER = "../shorts_fixed"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for video in os.listdir(INPUT_FOLDER):

    if video.endswith(".mp4"):

        input_path = os.path.join(INPUT_FOLDER, video)
        output_path = os.path.join(OUTPUT_FOLDER, video)

        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            "-vf", "scale=720:1280,setsar=1",
            "-c:v", "libx264",
            "-c:a", "aac",
            output_path
        ])

        print(f"Converted: {video}")

print("All videos converted to Shorts format!")
