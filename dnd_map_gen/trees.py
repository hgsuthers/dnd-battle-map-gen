from bases import Structure
from bases import BaseFlora

class Tree(Structure):
    def __init__(self, biome, name, color, weighting, tags=["tree"]):
        super().__init__(biome, name, color, weighting, tags)

class SwampTree(BaseFlora):
    def __init__(self, biome="swamp", name="SwampTree", abbr="ST1", color="dark olive green", weighting=10, tags=["flora"]):
        super().__init__(biome, name, abbr, color, weighting, tags)
