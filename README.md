# 🎬 YouTube Shorts Automation Pipeline

An end-to-end automation pipeline that transforms long videos into multiple YouTube Shorts using Python, FFmpeg, AI narration, and Google Cloud authentication.

---

## 🚀 Features

* 🔹 Split long videos into short clips
* 🔹 Generate narration using ElevenLabs AI
* 🔹 Merge audio narration with video clips
* 🔹 Convert videos to vertical (9:16) Shorts format
* 🔹 Upload videos using YouTube Data API
* 🔹 Schedule uploads (e.g. 3 videos/day)

---

## 🧠 Tools & Technologies

* Python (developed using Visual Studio Code)
* FFmpeg (video processing)
* ElevenLabs (AI voice narration)
* Google Cloud (OAuth 2.0 authentication)
* YouTube Data API (automated upload & scheduling)

---

## ⚙️ Pipeline Overview

```text id="u09h4x"
Long Video
   ↓
Split into clips
   ↓
Generate narration (ElevenLabs)
   ↓
Merge audio + video
   ↓
Convert to vertical Shorts format
   ↓
Upload & schedule via YouTube API (Google Cloud OAuth)
```

---

## 🔐 Authentication Setup (Google Cloud)

To enable automated uploads:

1. Create a project in Google Cloud Console
2. Enable **YouTube Data API v3**
3. Configure OAuth consent screen
4. Create OAuth Client ID (Desktop App)
5. Download credentials file

```text id="eqmjvn"
client_secrets.json
```

---

## 📁 Project Structure

```text id="j14f1g"
shorts-automation-pipeline/
│
├── video/           # Input long videos
├── output/          # Split clips
├── voice/           # AI-generated narration (ElevenLabs)
├── final/           # Merged videos
├── shorts_fixed/    # Vertical Shorts (ready for upload)
│
├── script/          # Python scripts (VS Code)
│   ├── split_video.py
│   ├── merge_voice.py
│   ├── convert_to_shorts.py
│   ├── upload_shorts.py
│   └── auto_upload_schedule.py
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

```bash id="3ukqlt"
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Split video

```bash id="wryq4y"
python script/split_video.py
```

### 2. Generate narration (ElevenLabs)

Save generated audio files in:

```text id="8x7c2o"
voice/
```

---

### 3. Merge audio

```bash id="g4gwm0"
python script/merge_voice.py
```

---

### 4. Convert to Shorts format

```bash id="93snql"
python script/convert_to_shorts.py
```

---

### 5. Upload to YouTube

```bash id="4fs5ap"
python script/upload_shorts.py
```

---

### 6. Schedule uploads

```bash id="3qrcs5"
python script/auto_upload_schedule.py
```

---

## ⚠️ Important Notes

* Shorts must be:

  * ≤ 60 seconds
  * Vertical (9:16)

* API Limits:

  * ~6 uploads/day (quota)
  * ~15 uploads/day (YouTube limit)

---

## 🎯 Example Output

* Input: 10-minute video
* Output: 40–50 Shorts
* Upload: Automated
* Scheduling: 3 videos/day

---

## 🔮 Future Improvements

* Auto subtitle generation
* AI script generation
* Smart highlight detection
* Multi-channel support

---

## 📌 Disclaimer

This project is for educational and automation purposes only.
