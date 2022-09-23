import json
import os

import youtube_uploader

if __name__ == "__main__":

    vid_metadata = youtube_uploader.default_upload_params()
    print(f"Video metadata: {json.dumps(vid_metadata, indent=2)}")

    youtube_uploader.upload(**vid_metadata)
    youtube_uploader.list_videos()
