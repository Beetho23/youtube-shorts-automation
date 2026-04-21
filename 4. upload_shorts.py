"""
Upload videos to YouTube (Private)
"""

import os
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

for video in os.listdir(VIDEO_FOLDER):

    if video.endswith(".mp4"):

        file_path = os.path.join(VIDEO_FOLDER, video)

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": video.replace(".mp4", ""),
                    "description": "AI generated Shorts #shorts",
                    "tags": ["shorts", "ai", "story"],
                    "categoryId": "22"
                },
                "status": {
                    "privacyStatus": "private"
                }
            },
            media_body=googleapiclient.http.MediaFileUpload(file_path)
        )

        request.execute()

        print(f"Uploaded: {video}")

print("All videos uploaded!")
