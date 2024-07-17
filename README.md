# yt-viewer
List YouTube videos you are subscribed to.

## How to install package
```bash
pip install -e git+https://github.com/VisualDudek/yt-viewer.git#egg=yt_viewer
```

# Dev notes
- [yt data API PlaylistItems](https://developers.google.com/youtube/v3/docs/playlistItems#resource)
    - JSON resource representation for `playlistItems` is not correct (!!!) -> `contentDetail` and `status` are optional.

## Python package naming

In Python package naming, hyphens (-) are not allowed in module names. This is because hyphens are not valid characters for Python identifiers, which means you cannot use them in import statements. Instead, underscores (_) are typically used in package names if you need a separator.

**Correct Package Naming**
When creating a Python package, you should adhere to these guidelines for naming:

1. Use Underscores Instead of Hyphens.
2. Use all lowercase letters for the package name.
3. Avoid Special Characters, only use letters, numbers, and underscores.