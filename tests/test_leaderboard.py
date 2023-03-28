import pytest
import sys
from pytest import fixture
import requests
from src.art_of_rally_leaderboard.leaderboard import Leaderboard 
# import vcr
from .board_entries import API_RESULT
board = Leaderboard(default_platform=5)


class MockResponse:
    def __init__(self):
        self.status_code = 200

    @staticmethod
    def json():
        return API_RESULT


    def raise_for_status(self):
        return None 


@fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, 'get', mock_get)


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


def test_top_ten(user_keys, mock_response):
    top_10 = board.top_ten("Finland", "Palus", "GroupB", direction="Reverse", wx="Rain")
    assert isinstance(top_10, dict)
    assert set(user_keys).issubset(top_10['leaderboard'][0].keys())
    assert len(top_10['leaderboard']) == 10

def test_capitalized_word(user_keys, mock_response):
    top_10 = board.top_ten("finland", "palus", 'Group2', "forward", "dry")
    assert isinstance(top_10, dict)
    assert top_10 != {'result': 0, 'leaderboard': []}
    assert  set(user_keys).issubset(top_10['leaderboard'][0].keys())
    assert len(top_10['leaderboard']) == 10

def test_url_build(capfd):
    url = board.build_url("Finland", "Palus", "Group2", "Forward", "Dry")
    assert url == "https://www.funselektorfun.com/artofrally/leaderboard/Finland_Stage_3_Forward_Dry_60s/0/5"

    input_test = board.build_url("fornland", "Palus", "Group2", "Forward", "Dry")
    captured = capfd.readouterr()
    assert captured.out == "Check your spelling and capitalization. Areas need capitalization example: Finland, Sardinia, Japan, Norway, Indonesia. Stages need correct spelling example: Indonesia mount kawi, not kawaii or kawai\n"
    input_test2 = board.build_url("Finland", "palus", "group2", "Fwd", "dry")
    captured2 = capfd.readouterr()
    assert captured.out == "Check your spelling and capitalization. Areas need capitalization example: Finland, Sardinia, Japan, Norway, Indonesia. Stages need correct spelling example: Indonesia mount kawi, not kawaii or kawai\n"

