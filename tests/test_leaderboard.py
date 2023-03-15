import pytest
from pytest import fixture
import requests
from src.art_of_rally_leaderboard.leaderboard import Leaderboard 
import vcr
board = Leaderboard(default_platform=5)

@fixture
def user_keys():
    return ["uniqueID", "userName", "rank", "score", "country", "carID", "replayData",  "platformID", "userID"]

@vcr.use_cassette('tests/vcr_cassettes/leaderboard_info.yml')
def test_top_ten(user_keys):
    top_10 = board.top_ten("Finland", "Palus", "GroupB", direction="Reverse", wx="Rain")
    assert isinstance(top_10, dict)
    assert set(user_keys).issubset(top_10['leaderboard'][0].keys())
    assert len(top_10['leaderboard']) == 10

@vcr.use_cassette('tests/vcr_cassettes/leaderboard_uppercase.yml')
def test_capitalized_word(user_keys):
    top_10 = board.top_ten("finland", "palus", 'Group2', "forward", "dry")
    assert isinstance(top_10, dict)
    assert top_10 != {'result': 0, 'leaderboard': []}
    assert  set(user_keys).issubset(top_10['leaderboard'][0].keys())
    assert len(top_10['leaderboard']) == 10


@vcr.use_cassette('tests/vcr_cassettes/leaderboard_status_check.yml')
def test_wrong_status(user_keys):
    with pytest.raises(Exception) as e:
        r = requests.get("https://www.funselektorfun.com/artofralllllly/leaderboard/Finland_Stage_1_Forward_Wet_60s")
        assert e.type == HTTPError

@vcr.use_cassette('tests/vcr_cassettes/leaderboard_key_error.yml')
def test_wrong_argument_value():
    with pytest.raises(KeyError):
        top_10 = board.top_ten("Fonland", "palus", "Group4","forward", "dry")
        

