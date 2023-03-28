import requests
import os
from .stage_dict import STAGES, GROUPS, WEATHER, DIRECTION

class Leaderboard:

    def __init__(self, my_id=None, default_platform=2):
        self.my_id = my_id
        self.default_platform = default_platform
        self.url="https://www.funselektorfun.com/artofrally/leaderboard"


    def build_url(self, area, stage, group, direction, wx):
        try:
            area = area.title()
            stage = stage.lower()
            stage = STAGES[area][stage]
            group = GROUPS[group]
            direction = DIRECTION[direction]
            wx = WEATHER[wx]
        except KeyError as e:
            print("Check your spelling and capitalization. Areas need capitalization example: Finland, Sardinia, Japan, Norway, Indonesia. Stages need correct spelling example: Indonesia mount kawi, not kawaii or kawai")

        url = f"{self.url}/{area}_Stage_{stage}_{direction}_{wx}_{group}/0/{self.default_platform}" 
        return url


    def top_ten(self, area, stage, group, direction="Forward", wx="Dry"):
        url = self.build_url(area, stage, group, direction, wx) 
        r = requests.get(url)
        r.raise_for_status()
        return r.json()


    def my_standing(self):
        pass

    def full_list(self):
        pass



# https://github.com/Theaninova/ArtOfRallyLeaderboardAPI/tree/master/leaderboard-connection/leaderboard-string
