from pytest import fixture
from lb_wrapper import top_ten
import vcr


@fixture
def user_keys():
    return ["uniqueID", "userName", "rank", "score", "country", "carID", "replayData",  "platformID", "userID"]

@vcr.use_cassette('tests/vcr_cassettes/leaderboard_info.yml')
def test_top_ten(user_keys):
    top_10 = top_ten("Finland", "Palus", "60s", direction="Reverse", wx="Wet")
    assert isinstance(top_10, dict)
    assert set(user_keys).issubset(top_10['leaderboard'][0].keys())

@vcr.use_cassette('tests/vcr_cassettes/leaderboard_uppercase.yml')
def test_capitalized_word(user_keys):
    top_10 = top_ten("finland", "palus", "60s","forward", "dry")
    assert isinstance(top_10, dict)
    assert top_10 != {'result': 0, 'leaderboard': []}
    assert  set(user_keys).issubset(top_10['leaderboard'][0].keys())
