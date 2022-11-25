import random
class MapGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.total_buildings = 0
        self.struct_list = []
        self.grid = self.create_grid()

    def create_grid(self):
        '''Simply return a blank matrix.'''
        return [['' for c in range(self.cols)] for r in range(self.rows)]

    def place_random_at_point(self, row, col, struct_list, objects_lookup):
        '''
        Place a random structure at given row,col point.
        
        Takes a random structure from struct_list and finds it in
         the object lookup table.

        Place the object by assigning it to a [row][col] position on the grid.
        '''
        choice = random.choice(struct_list)
        rand_obj = objects_lookup[choice]()

        self.grid[row][col] = rand_obj
        return None

    def place_specific(self, row, col, obj):
        '''
        Place a tile at a specific point.
        
        Place the object denoted in the parameters at the given [row][col]
         position on the grid.
        '''
        self.grid[row][col] = obj

    def place_random(self, struct_list, objects_lookup):
        '''
        Place a random object in a random location.
        
        Find a random [row][col] position on the grid and
         place a random object chosen from struct_list.
        '''
        rand_row = random.randint(0, self.rows-1)
        rand_col = random.randint(0, self.cols-1)

        choice = random.choice(struct_list)
        rand_obj = objects_lookup[choice]()

        self.grid[rand_row][rand_col] = rand_obj
        return None

    def initialize_field(self, n, struct_list, objects_lookup):
        '''
        Place N number of random tiles.
        
        Simply place a number of random objects at random [row][col]
         positions on the grid.
        '''
        for i in range(n):
            self.place_random(struct_list, objects_lookup)
        return None

    def place_weighted(self,
        struct_list,
        capped_list,
        objects_lookup,
        weights,
        num_buildings,
        i,
        j
    ):
        weights_list = []

        '''
        Place a block, weighted based on surrounding blocks.
        '''
        # iterate over every structure in struct_list based on the
        #  four tiles that surround the current tile

        # the current tile is grid[i][j], so we need to iterate over
        # i+1, j; i-1, j; i, j+1; i, j-1
        for struct in struct_list:
            try:
                # start by looking at i+1, j
                # if the name of the tile at i+1, j is the same
                #  as the current struct being iterated over then 
                #  add the weighting of the structure at i+1, j to our
                #  weights dictionary
                name = self.grid[i+1][j].name
                if name == struct:
                    weights[struct] += self.grid[i+1][j].weighting
            except AttributeError:
                '''There's an empty string at the location.'''
                pass
            except IndexError:
                '''Max row has been reached.'''
                pass
            try:
                name = self.grid[i-1][j].name
                if name == struct:
                    weights[struct] += self.grid[i-1][j].weighting
            except AttributeError:
                '''There's an empty string at the location.'''
                pass
            except IndexError:
                '''Min row has been reached.'''
                pass
            try:
                name = self.grid[i][j+1].name
                if name == struct:
                    weights[struct] += self.grid[i][j+1].weighting
            except AttributeError:
                '''There's an empty string at the location.'''
                pass
            except IndexError:
                '''Max col has been reached.'''
                pass
            try:
                name = self.grid[i][j-1].name
                if name == struct:
                    #total_weights[struct] += 15
                    weights[struct] += self.grid[i][j-1].weighting
            except AttributeError:
                '''There's an empty string at the location.'''
                pass
            except IndexError:
                '''Min col has been reached.'''
                pass

        # transfer the weighting dict to a list that matches struct_list
        #  weights_list[0] is the weighting at struct_list[0]
        for struct in struct_list:
            weights_list.append(weights[struct])

        # if a calculation cant be made, just place a random block
        if sum(weights_list) <= 15:
            self.place_random_at_point(i, j, struct_list, objects_lookup)
        # else, use the weighting we derived by checking surrounding blocks
        else:
            choice = random.choices(struct_list, weights=weights_list, k=1)[0]
            self.grid[i][j] = objects_lookup[choice]()

        # should be its own method
        # remove any buildings from struct list if cap is hit
        if self.total_buildings >= num_buildings:
            for struct in struct_list:
                if "building" in objects_lookup[struct]().tags:
                    if struct not in capped_list:
                        capped_list.append(struct)
        # now actually remove the buildings
        for struct in capped_list:
            if struct in struct_list:
                struct_list.remove(struct)

        if "building" in self.grid[i][j].tags:
            self.total_buildings += 1

        if "elevated" in self.grid[i][j].tags:
            self.grid[i][j].elevation = self.grid[i][j].calculate_elevation()

        return None
        #print(weights_list)
    
    def handle_right_square():
        return None

