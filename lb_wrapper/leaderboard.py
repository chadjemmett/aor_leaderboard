import requests

URL = "https://www.funselektorfun.com/artofrally/leaderboard"


# r = requests.get("https://www.funselektorfun.com/artofrally/leaderboard/Finland_Stage_1_Forward_Dry_60s/0/1")

# print(r.text)


def top_ten(area, stage, direction, wx, group):
    r = requests.get(f"{URL}/{area}_Stage_{stage}_{direction}_{wx}_{group}/0/1")
    return r.text




print(top_ten('Finland', '1', 'Forward', 'Dry', '60s'))
