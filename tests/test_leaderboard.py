import pytest
import sys
from pytest import fixture
import requests
from src.art_of_rally_leaderboard.leaderboard import Leaderboard 
import vcr
board = Leaderboard(default_platform=5)

@fixture
def user_keys():
    return ["uniqueID", "userName", "rank", "score", "country", "carID", "replayData",  "platformID", "userID"]

@fixture
def key_error_message():

    return  """
        KeyError
        Check your capitalization. 
        Example: GroupB or Lake Kawi
                    """


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
def test_wrong_argument_value(capfd):
    top_10 = board.top_ten("Fonland", "palussss", "Group44","forward", "dry")
    assert top_10 == {'result': 0, 'leaderboard': []}
    captured = capfd.readouterr()
    assert captured.out == "Check your capitalization or spelling. Stage example: San Benedetto. Group Example: GroupB.\n"

