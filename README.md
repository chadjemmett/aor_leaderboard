## Art of Rally Leaderboard Python Library

[Art of Rally](https://www.funselektor.com/) by FunSelektor is a multi-platform arcade-style racing game. Drivers can compete against other drivers via the
leaderboard. You can check your standings in game, but this is for getting leaderboards from the API endpoint.

Any questions? Contact me on Github at `https://github.com/chadjemmett` and I'm
`mini_robber/Chad/Chood` on the Art of Rally Discord.


### Usage

*Note: The API URLs are case-sensetive. So if something isn't working capitalize the value you pass into the functions*

#### Installation: ` pip install -i https://test.pypi.org/simple/ aor-leaderboard-py`

 ``` 
>>> from aor_leaderboard_py import art_of_rally_leaderboard Leaderboard`
>>> board = Leaderboard(default_platform="2")`
>>> board.top_ten("Finland", "Palus", "Group2", direction="Forward", wx="Dry")

 {'result': 0, 'leaderboard': 

    [{'uniqueID': 61, 'userName': 'coXXXney', 'rank': 1, 'score': 182017, 'country': 166, 'carID': 2, 'replayData': 'dt7-h01v2Sa7OPgvnpDOnO6igys', 'platformID': 5, 'userID': 'Switch_227XXXXXXXX65AFB'},  
...
 {'uniqueID': 181, 'userName': 'XXXn', 'rank': 9, 'score': 220556, 'country': 23, 'carID': 0, 'replayData': 'EnV9-dQXXXgiT2aG_S72DZgtaBo', 'platformID': 5, 'userID': 'Switch_EF9EXXXXXXXXCA8B'}, 

 {'uniqueID': 384, 'userName': 'TXXXn', 'rank': 10, 'score': 221566, 'country': 166, 'carID': 5, 'replayData': 'TzGJ267q0XXXXXXXXY_WM8Iab1Q', 'platformID': 5, 'userID': 'Switch_37F9E0XXXXX20FF2'}]

```
 Right now the default platform is Steam. These are all the platforms and their codes.
 You can set the default when invoking the class. `board = Leaderboard(default_platform=4)` if you want to get leaderboards for Playstation.
 
      Epic: 0,
      GOG: 1,
      Steam: 2,
      Xbox: 3,
      PlayStation: 4,
      Nintendo: 5,
      None: 6

The values for the Group variable are as follows:
```
  "Group2",
  "Group3", 
  "Group4",
  "GroupB",
  "GroupS",
  "GroupA",
  "Vans",
  "Triwheeler",
  "Trucks",
  "Logging"

```


Area, Stage and group are required. The default for stages is direction = Forward. And wx = Dry

The two options for Direction is Forward or Reverse, and Wx's options are Wet or Dry 


### Thanks to...
This Python Library pulls heavily from the work of [Thea Schöbl](https://github.com/Theaninova) Who put together all of
the API documentation in one place here: [ArtOfRallyLeaderboardAPI](https://github.com/Theaninova/ArtOfRallyLeaderboardAPI)
Please send a thanks for the hard work.
