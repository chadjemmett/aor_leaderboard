import requests
from .stage_dict import stages, groups
chad_id = "Switch_C932B380835E956A"
URL = "https://www.funselektorfun.com/artofrally/leaderboard"

def top_ten(area, stage, group, direction="Forward", wx="Dry"):
    #capitalize all the args
    area = area.title()
    stage = stage.title()
    stage = stages[area][stage] 
    direction = direction.title()
    wx = wx.title()
    #make request and return
    url = f"{URL}/{area}_Stage_{stage}_{direction}_{wx}_{group}/0/5"
    r = requests.get(url)
    return r.json()

# https://github.com/Theaninova/ArtOfRallyLeaderboardAPI/tree/master/leaderboard-connection/leaderboard-string
