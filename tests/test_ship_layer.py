from types import SimpleNamespace

from PIL import Image

from renderer.layers.ship import LayerShipBase


class TrackingResourceManager:
    def __init__(self):
        self.loaded = []

    def load_image(self, filename, **kwargs):
        self.loaded.append(filename)
        return Image.new("RGBA", kwargs["size"])


def test_unknown_active_consumable_is_skipped_without_aborting_render():
    resources = TrackingResourceManager()
    renderer = SimpleNamespace(
        conman=SimpleNamespace(active_consumables={7: {42: 30, 44: 30}}),
        resman=resources,
    )
    layer = LayerShipBase.__new__(LayerShipBase)
    layer._renderer = renderer
    layer._abilities = {
        123: {"id_to_index": {}},
        "clan": {44: "PXY630_TacticalMinefield"},
    }
    layer._consumable_cache = {}

    layer._ship_consumable(Image.new("RGBA", (64, 64)), vehicle_id=7, params_id=123)

    assert resources.loaded == ["consumable_PXY630_TacticalMinefield.png"]
