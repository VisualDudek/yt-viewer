# yt-viewer
List YouTube videos you are subscribed to.

# Dev notes
- [yt data API PlaylistItems](https://developers.google.com/youtube/v3/docs/playlistItems#resource)
    - JSON resource representation for `playlistItems` is not correct (!!!) -> `contentDetail` and `status` are optional.
