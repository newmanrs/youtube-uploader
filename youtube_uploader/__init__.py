import json
import os
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo


def _load_secrets_loc():

    secrets = os.getenv("CLIENT_SECRETS_YT_API")
    if secrets is None:
        raise EnvironmentError("Please export $CLIENT_SECRETS_YT_API")
    return os.path.expanduser(secrets)


def list_videos():

    channel = Channel()
    channel.login(_load_secrets_loc(), "credentials.storage")
    videos = channel.fetch_uploads()

    for video in videos:
        m = f"Video id: {video.id}"
        m += f" URL: https://youtube.com/watch?v={video.id}\n"
        m += f" Title: {video.title}\n"
        print(m)


def default_upload_params():

    return {
        "video": "test_video.mp4",
        "title": "Video Title",
        "description": "Video Description",
        "thumbnail": "test_thumb.png",
        "tags": ["tag1", "tag2"],
        "category": "education",
        "lang": "en-US",
        "embeddable": True,
        "license": "creativeCommon",
        "stats_viewable": True,
    }


def upload(
    video,
    title,
    description,
    thumbnail,
    tags,
    category,
    lang,
    embeddable,
    license,
    stats_viewable,
):

    channel = Channel()
    channel.login(_load_secrets_loc(), "credentials.storage")

    # setting up the video
    video = LocalVideo(video)

    # setting snippet
    video.set_title(title)
    video.set_description(description)
    video.set_tags(tags)
    video.set_category(category)
    video.set_default_language(lang)

    # setting status
    video.set_embeddable(embeddable)
    video.set_license(license)
    video.set_privacy_status("public")
    video.set_public_stats_viewable(stats_viewable)

    # setting thumbnail
    video.set_thumbnail_path(thumbnail)

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)

    # liking video
    video.like()
