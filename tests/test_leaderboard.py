from pytest import fixture
from lb_wrapper import top_ten
import vcr


@fixture
def user_keys():
    return ["uniqueID", "userName", "rank", "score", "country", "carID", "replayData",  "platformID", "userID"]

@vcr.use_cassette('tests/vcr_cassettes/leaderboard_info.yml')
def test_top_ten(user_keys):
    top_10 = top_ten("Finland", "1", "Forward", "Dry", "60s")
    assert isinstance(top_10, dict)
    assert set(user_keys).issubset(top_10['leaderboard'][0].keys())
