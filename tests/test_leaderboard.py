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


# @vcr.use_cassette('tests/vcr_cassettes/leaderboard_key_error.yml')
def test_time_conversion(monkeypatch):

    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = 'htts://something/api/leaderboard/'
            self.raise_for_status = KeyError

        def json(self):
            return {'result': 0, 'leaderboard': [{'uniqueID': 30614, 'userName': 'Toucan', 'rank': 1, 'score': 161031, 'country': 165, 'carID': 0, 'replayData': 'khk3PEU1jz9a8_SfVt5K1w81pnE', 'platformID': 2, 'userID': '76561198354051785'}, {'uniqueID': 33582, 'userName': 'Proporo', 'rank': 2, 'score': 144300, 'country': 52, 'carID': 0, 'replayData': 'aOBc0rTzzXHYBh14sb-DWkZzRNY', 'platformID': 2, 'userID': '76561197960981627'}, {'uniqueID': 99, 'userName': 'PlayerZ', 'rank': 3, 'score': 144993, 'country': 98, 'carID': 2, 'replayData': 'vSJ6nG826bAQWuA-UNEnw-I6qhk', 'platformID': 2, 'userID': '76561198262925215'}, {'uniqueID': 7, 'userName': 'Myth', 'rank': 4, 'score': 146733, 'country': 9, 'carID': 0, 'replayData': 'vQbd7w8CFPenKumK22yutHeButE', 'platformID': 2, 'userID': '76561198009321752'}, {'uniqueID': 41948, 'userName': 'turbo', 'rank': 5, 'score': 146827, 'country': 165, 'carID': 0, 'replayData': 'QDwcKucQO4mzSccseSKfuKqDE6U', 'platformID': 2, 'userID': '76561198089118617'}, {'uniqueID': 35963, 'userName': 'Colorcat23', 'rank': 6, 'score': 147315, 'country': 57, 'carID': 0, 'replayData': 'S5AscT1MDMuH6kAYIss2It4TsmA', 'platformID': 3, 'userID': ''}, {'uniqueID': 14, 'userName': 'imcalfin', 'rank': 7, 'score': 147791, 'country': 52, 'carID': 3, 'replayData': 'pJerHEpZcd6NSPS7NfSWemHAMcA', 'platformID': 1, 'userID': ''}, {'uniqueID': 328, 'userName': 'Lee Boon', 'rank': 8, 'score': 147825, 'country': 77, 'carID': 0, 'replayData': 'FjgOB2uXQ9mpTeXsQGCxxghHUcA', 'platformID': 2, 'userID': '76561198031929915'}, {'uniqueID': 58880, 'userName': 'domer', 'rank': 9, 'score': 148271, 'country': 6, 'carID': 0, 'replayData': '1aA27xP66YbfbtZtm_rkUHB6nBs', 'platformID': 2, 'userID': '76561198073829117'}, {'uniqueID': 24760, 'userName': 'Hulter', 'rank': 10, 'score': 148322, 'country': 52, 'carID': 1, 'replayData': 'zUPnhjvmTdDrhBnzENwfxU1LbpE', 'platformID': 2, 'userID': '76561198116534013'}]}
    def mock_get(url):
        return MockResponse()
    


    monkeypatch.setattr(requests, 'get', mock_get)
    top_10 = board.top_ten("Finland", "Palus", "Group2")
    time = top_10['leaderboard'][0]['score']
    assert isinstance(top_10, dict)

    assert time == "02:41.031"


