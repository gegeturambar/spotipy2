from __future__ import annotations
from typing import List, Optional

import spotipy2
from spotipy2.types import Show
from spotipy2.types.paging import Paging


class ShowMethods:
    async def get_shows(
        self: spotipy2.Spotify, show_ids: List[str]  # type: ignore
    ) -> List[Show]:
        shows = await self._get(
            "shows", params={"ids": ",".join([self.get_id(i) for i in show_ids])}
        )
        return shows["shows"]

    async def get_show(self: spotipy2.Spotify, show_id: str) -> Show:  # type: ignore
        return await self._get(f"shows/{self.get_id(show_id)}")

    async def get_show_tracks(
        self: spotipy2.Spotify,  # type: ignore
        show_id: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Paging:
        params = self.wrapper(market=market, limit=limit, offset=offset)

        show_tracks = await self._get(
            f"shows/{self.get_id(show_id)}/tracks", params=params
        )
        return show_tracks
