from __future__ import annotations
from typing import List, Optional

import spotipy2
from spotipy2.types import Episode


class EpisodeMethods:
    async def get_episodes(
        self: spotipy2.Spotify, episode_ids: List[str]  # type: ignore
    ) -> List[Episode]:
        r = await self._get(
            "episodes", params={"ids": ",".join([self.get_id(i) for i in episode_ids])}
        )

        return r["episodes"]

    async def get_episode(self: spotipy2.Spotify, episode_id: str) -> Episode:  # type: ignore
        return await self._get(f"episodes/{self.get_id(episode_id)}")

    async def get_recommendations(
        self: spotipy2.Spotify,
        artist_ids: Optional[List[str]] = None,
        episode_ids: Optional[List[str]] = None,
        genre_names: Optional[List[str]] = None,
        limit: Optional[int] = None,
        market: Optional[str] = None,
        **kwargs,
    ) -> List[Episode]:
        """Returns recommended episodes based on given artist, episode or genre seeds.
        Note the names in `genres_names` have to be one of availabe genres accessible
        via the `get_recommendation_genres` function
        #### Keyword arguments:
          - `min/max/target_<attribute>` - For the tuneable episode
                    attributes listed in the documentation, these values
                    provide filters and targeting on results.
        """
        assert any(
            [artist_ids, episode_ids, genre_names]
        ), "You have to specify at least one seed to get recommendations based on"

        # Mering with `kwargs` to include the tuneable attributes as well
        params = {**self.wrapper(market=market, limit=limit), **kwargs}

        if artist_ids:
            params["seed_artists"] = ",".join(list(map(self.get_id, artist_ids)))
        if episode_ids:
            params["seed_episodes"] = ",".join(list(map(self.get_id, episode_ids)))
        if genre_names:
            params["seed_genres"] = ",".join(genre_names)

        r = await self._get("recommendations", params)
        return r["episodes"]

    async def get_recommendation_genres(self: spotipy2.Spotify) -> List[str]:
        """Returns a list of genre names to be used as `genre_names`
        argument of the `get_recommendations` function
        """
        r = await self._get("recommendations/available-genre-seeds")
        return r["genres"]
