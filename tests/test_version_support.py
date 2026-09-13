from replay_unpack.clients.wows.helper import get_controller


def test_wows_15_8_0_has_a_controller():
    controller = get_controller("15_8_0")

    assert controller.__class__.__name__ == "BattleController"
