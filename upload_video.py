import json
import os

import youtube_uploader

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            vid_metadata = json.load(f)
    else:
        raise ValueError("Provide video metadata json as script argument")


    #youtube_uploader.upload(**vid_metadata)
    youtube_uploader.list_videos()
