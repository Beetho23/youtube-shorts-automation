"""
Upload + Schedule 3 videos per day
"""

import os
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.http

CLIENT_SECRET_FILE = "client_secrets.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

VIDEO_FOLDER = "../shorts_fixed"

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_FILE, SCOPES
)

credentials = flow.run_local_server(port=0)

youtube = googleapiclient.discovery.build(
    "youtube", "v3", credentials=credentials
)

videos = sorted(os.listdir(VIDEO_FOLDER))
start_date = datetime.datetime.utcnow()

for i, video in enumerate(videos):

    if video.endswith(".mp4"):

        file_path = os.path.join(VIDEO_FOLDER, video)

        day_offset = i // 3
        hour = 12 + (i % 3) * 3

        publish_time = start_date + datetime.timedelta(days=day_offset)
        publish_time = publish_time.replace(hour=hour, minute=0, second=0)

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": video.replace(".mp4", ""),
                    "description": "Automated Shorts #shorts",
                    "tags": ["shorts", "automation"],
                    "categoryId": "22"
                },
                "status": {
                    "privacyStatus": "private",
                    "publishAt": publish_time.isoformat() + "Z"
                }
            },
            media_body=googleapiclient.http.MediaFileUpload(file_path)
        )

        request.execute()

        print(f"Scheduled: {video} → {publish_time}")

print("All videos scheduled!")
