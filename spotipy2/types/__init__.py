from .base import BaseType
from .paging import Paging
from .album import Album
from .show import Show
from .episode import Episode
from .artist import Artist
from .playlist import Playlist
from .track import Track
from .user import User
from .playlist_item import PlaylistItem

SPOTIFY = {
    "album": Album,
    "show": Show,
    "episode": Episode,
    "artist": Artist,
    "playlist": Playlist,
    "track": Track,
    "user": User
}

__all__ = [
    "BaseType",
    "Paging",
    "Album",
    "Episode",
    "Show",
    "Artist",
    "Playlist",
    "Track",
    "User",
    "PlaylistItem"
]
