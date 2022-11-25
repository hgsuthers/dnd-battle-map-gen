from bases import Structure
from bases import BaseLand

class SwampLand(BaseLand):
    def __init__(self, biome="swamp", name="SwampLand", abbr="SL1", color="OliveDrab4", weighting=23, tags=["land", "elevated"]):
        super().__init__(biome, name, abbr, color, weighting, tags)

    def __str__(self):
        return str(self.elevation)

class SwampLand2(BaseLand):
    def __init__(self, biome="swamp", name="SwampLand2", abbr="SL2", color="OliveDrab3", weighting=23, tags=["land", "elevated"]):
        super().__init__(biome, name, abbr, color, weighting, tags)

    # briefly overload the str method to show us elevation
    def __str__(self):
        return str(self.elevation)