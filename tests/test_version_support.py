from importlib import import_module

from replay_unpack.clients.wows.helper import get_controller


def test_wows_15_8_0_has_a_controller():
    controller = get_controller("15_8_0")

    assert controller.__class__.__name__ == "BattleController"


def test_wows_15_9_0_supports_new_player_property_mapping():
    controller = get_controller("15_9_0")
    constants = import_module(
        "replay_unpack.clients.wows.versions.15_9_0.constants"
    )

    assert controller.__class__.__name__ == "BattleController"
    assert constants.id_property_map[33] == "shipFrags"
    assert constants.id_property_map[34] == "shipId"
    assert constants.id_property_map_bots[23] == "shipFrags"
