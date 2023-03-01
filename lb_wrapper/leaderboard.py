import requests
from stage_dict import stages
chad_id = "Switch_C932B380835E956A"
URL = "https://www.funselektorfun.com/artofrally/leaderboard"



def top_ten(area, stage, direction, wx, group):
    stage = stages[area.title()][stage.title()]
    # print(stage)
    url = f"{URL}/{area}_Stage_{stage}_{direction}_{wx}_{group}/0/5"
    print(url)
    r = requests.get(url)
    return r.json()

print(top_ten('japan', 'Nikko', 'Forward', 'Dry', '60s'))
# https://github.com/Theaninova/ArtOfRallyLeaderboardAPI/tree/master/leaderboard-connection/leaderboard-string
