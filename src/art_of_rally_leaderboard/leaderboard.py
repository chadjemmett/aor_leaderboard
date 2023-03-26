import requests
import os
from .stage_dict import STAGES, GROUPS, WEATHER

class Leaderboard:

    def __init__(self, my_id=None, default_platform=2):
        self.my_id = my_id
        self.default_platform = default_platform
        self.url="https://www.funselektorfun.com/artofrally/leaderboard"


    def top_ten(self, area, stage, group, direction="Forward", wx="Dry"):
        #capitalize all the args
        area = area.title()
        stage = stage.title()
        self.check_input_cases(area, stage, group)
        direction = direction.title()
        try:
            stage = STAGES[area].get(stage) 
            wx = WEATHER[wx.title()]
            group = GROUPS[group]
        except KeyError as e:
            print("Check your capitalization or spelling. Stage example: San Benedetto. Group Example: GroupB.")
        #make request and return
        url = f"{self.url}/{area}_Stage_{stage}_{direction}_{wx}_{group}/0/{self.default_platform}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()


    def my_standing(self):
        pass

    def full_list(self):
        pass



# https://github.com/Theaninova/ArtOfRallyLeaderboardAPI/tree/master/leaderboard-connection/leaderboard-string
