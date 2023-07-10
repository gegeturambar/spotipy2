import re

from .albums import AlbumMethods
from .shows import ShowMethods
from .episodes import EpisodeMethods
from .artists import ArtistMethods
from .search import SearchMethods
from .tracks import TrackMethods
from .playlists import PlaylistMethods
from .users import UserMethods


class Methods(
    AlbumMethods, ArtistMethods, SearchMethods, TrackMethods, PlaylistMethods, UserMethods, EpisodeMethods, ShowMethods
):
    @staticmethod
    def get_id(s: str) -> str:
        if m := re.search("(?!.*/).+", s):
            return m[0].split("?")[0]
        else:
            raise ValueError("ID not valid")

    @staticmethod
    def wrapper(**kwargs):
        return {k: v for k, v in kwargs.items() if v is not None}
