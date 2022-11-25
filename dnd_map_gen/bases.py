import json
class BaseLand:
    '''Parent class for all land and water tiles.'''
    def __init__(self, biome, name, abbr, color, weighting, tags):
        self.biome = biome
        self.name = name
        self.abbr = abbr
        self.color = color
        self.weighting = weighting
        self.tags = [tag for tag in tags]

    def calculate_elevation(self):
        '''Intelligently determine the elevation of a point given its neighbors.
        Could change based on type of land being placed.. land, mountain, hill.'''
        elev = 0

        return elev

    def __repr__(self):
        return self.name

    def jsonify(self):
        return json.dumps(self.__dict__)

class BaseFlora:
    '''Parent class for all flora.'''
    def __init__(self, biome, name, abbr, color, weighting, tags):
        self.biome = biome
        self.name = name
        self.abbr = abbr
        self.color = color
        self.weighting = weighting
        self.tags = [tag for tag in tags]

    def __repr__(self):
        return self.name

    def jsonify(self):
        return json.dumps(self.__dict__)

class BaseBuilding:
    '''Parent class for all buildings.'''
    def __init__(self, biome, name, abbr, color, weighting, tags):
        self.biome = biome
        self.name = name
        self.abbr = abbr
        self.color = color
        self.weighting = weighting
        self.tags = [tag for tag in tags]

###
class Structure:
    '''Parent class for all buildings, land masses, flora, and bodies of water.'''
    def __init__(self, biome, name, color, weighting, tags):
        self.biome = biome
        self.name = name
        self.color = color
        self.weighting = weighting
        self.tags = [tag for tag in tags]
        self.image = None

    def __repr__(self):
        return self.name

    def jsonify(self):
        return json.dumps(self.__dict__)

class Creature:
    '''Parent class to all NPCs and characters as well as fauna.'''
    def __init__(self):
        pass
