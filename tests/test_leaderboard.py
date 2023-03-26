import pytest
import sys
from pytest import fixture
import requests
from src.art_of_rally_leaderboard.leaderboard import Leaderboard 
import vcr
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


# def test_wrong_argument_value(capfd, mock_response):
#     top_10 = board.top_ten("Fonland", "palussss", "Group44","forward", "dry")
#     captured = capfd.readouterr()
#     assert captured.out == "Check your capitalization or spelling. Stage example: San Benedetto. Group Example: GroupB.\n"







