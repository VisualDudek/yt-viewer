from typing import Dict, Optional
from pydantic import BaseModel, constr
from datetime import datetime

class Thumbnail(BaseModel):
    url: str
    width: int
    height: int

class ResourceId(BaseModel):
    kind: str
    videoId: str

class Snippet(BaseModel):
    publishedAt: datetime
    channelId: str
    title: str
    description: str
    thumbnails: Dict[str, Thumbnail]
    channelTitle: str
    videoOwnerChannelTitle: str
    videoOwnerChannelId: str
    playlistId: str
    position: int
    resourceId: ResourceId

class ContentDetails(BaseModel):
    videoId: str
    startAt: Optional[str]
    endAt: Optional[str]
    note: Optional[str]
    videoPublishedAt: datetime

class Status(BaseModel):
    privacyStatus: str

class PlaylistItem(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: Snippet
    contentDetails: Optional[ContentDetails] = None
    status: Optional[Status] = None

# Example Usage
example_data = {
  "kind": "youtube#playlistItem",
  "etag": "someEtagValue",
  "id": "someId",
  "snippet": {
    "publishedAt": "2023-01-01T00:00:00Z",
    "channelId": "someChannelId",
    "title": "someTitle",
    "description": "someDescription",
    "thumbnails": {
      "default": {
        "url": "http://example.com/default.jpg",
        "width": 120,
        "height": 90
      },
      "medium": {
        "url": "http://example.com/medium.jpg",
        "width": 320,
        "height": 180
      },
      "high": {
        "url": "http://example.com/high.jpg",
        "width": 480,
        "height": 360
      }
    },
    "channelTitle": "someChannelTitle",
    "videoOwnerChannelTitle": "someVideoOwnerChannelTitle",
    "videoOwnerChannelId": "someVideoOwnerChannelId",
    "playlistId": "somePlaylistId",
    "position": 0,
    "resourceId": {
      "kind": "youtube#video",
      "videoId": "someVideoId"
    }
  },
  "contentDetails": {
    "videoId": "someVideoId",
    "startAt": "0:00",
    "endAt": "0:10",
    "note": "someNote",
    "videoPublishedAt": "2023-01-01T00:00:00Z"
  },
  "status": {
    "privacyStatus": "public"
  }
}

# playlist_item = PlaylistItem(**example_data)
# print(playlist_item)
