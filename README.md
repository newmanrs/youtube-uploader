# youtube-uploader

Quick interface for Youtube [built around](https://pypi.org/project/simple-youtube-api/).

# Setup

You will need to generate [Youtube APIv3](https://developers.google.com/youtube/v3/getting-started) OAuth2 keys.  Be careful in the GCP setup as you can enable the API but generate keys with only read access.  The use will require a browser login to generate an initial token.  The Youtube API has a quota credit system that allows up to 6 uploads per day, unless you file some forms to [request an audit](https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits).  See costs of API operations [here](https://developers.google.com/youtube/v3/determine_quota_cost).

# Usage


```python
import youtube_uploader
vid_desc = {"video": "test_video.mp4",
    "title": "Video Title",
    "description": "Video Description",
    "thumbnail": "test_thumb.png",
    "tags": ["tag1", "tag2"],
    "category": "education",
    "lang": "en-US",
    "embeddable": True,
    "license": "creativeCommon",
    "stats_viewable": True,
    "privacy_status": "public"}
youtube_uploader.upload(**vid_desc)
```
