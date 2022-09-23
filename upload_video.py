import json
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo


def upload_to_youtube(
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

    # login into the channel
    channel = Channel()
    channel.login("../youtube_oauth.json", "credentials.storage")

    # setting up the video that is going to be uploaded
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


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            vid_metadata = json.load(f)
        upload_to_youtube(**vid_metadata)
    else:
        raise ValueError("Provide metadata file as script argument")
