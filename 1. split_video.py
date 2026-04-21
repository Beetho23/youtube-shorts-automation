"""
Split a long video into 15-second clips
"""

import os
import subprocess
import math

INPUT_VIDEO = "../video/source.mp4"
OUTPUT_FOLDER = "../output"
CLIP_DURATION = 15

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def get_duration(video):
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            video
        ],
        stdout=subprocess.PIPE
    )
    return float(result.stdout)

duration = get_duration(INPUT_VIDEO)
total_clips = math.ceil(duration / CLIP_DURATION)

for i in range(total_clips):
    start = i * CLIP_DURATION
    output_file = f"{OUTPUT_FOLDER}/clip_{i+1}.mp4"

    subprocess.run([
        "ffmpeg",
        "-ss", str(start),
        "-i", INPUT_VIDEO,
        "-t", str(CLIP_DURATION),
        "-c", "copy",
        output_file
    ])

    print(f"Created: {output_file}")

print("All clips generated!")
