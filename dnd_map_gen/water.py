from bases import Structure

class Water(Structure):
    def __init__(self, biome, name, color, weighting, tags=["water"]):
        super().__init__(biome, name, color, weighting, tags)

class Bog(Water):
    def __init__(self, biome="swamp", name="Bog", color="DarkSeaGreen4", weighting=28):
        super().__init__(biome, name, color, weighting)