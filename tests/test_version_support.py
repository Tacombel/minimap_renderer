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


def test_58_ridge_new_map_has_manifest_and_assets():
    from importlib.resources import files

    from renderer.resman import ResourceManager

    manifest = ResourceManager("15_9_0").load_json("manifest.json", "spaces")
    assert manifest["58_RidgeNew"] == [760, 1600, 0.475]

    map_resources = files("maps.spaces.58_RidgeNew")
    assert map_resources.joinpath("minimap.png").is_file()
    assert map_resources.joinpath("minimap_water.png").is_file()

    renderer_resources = files("renderer.resources.spaces.58_RidgeNew")
    assert renderer_resources.joinpath("minimap.png").is_file()
    assert renderer_resources.joinpath("minimap_water.png").is_file()
