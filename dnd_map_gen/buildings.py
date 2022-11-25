from bases import Structure

class Building(Structure):
    def __init__(self, biome, name, color, weighting, tags=["building", "capped"]):
        super().__init__(biome, name, color, weighting, tags)

class Hut(Building):
    def __init__(self, biome="swamp", name="Hut", color="grey", weighting = 0):
        super().__init__(biome, name, color, weighting)