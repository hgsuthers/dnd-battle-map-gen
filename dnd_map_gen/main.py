from water import *
from land import *
from trees import *
from buildings import *
from grid import MapGrid
import tkinter as tk
from config import structure_map

window = tk.Tk()

type_of_map = "swamp"
list_of_things = []

def create_list_of_structures(map_type):
    '''
    Create a list of structures based on the inputted map type.

    Iterate over the structure_map in config.py looking for 
        map_type. Once map_type is found, iterate over and append
        all of the values inside of the map_type sub-dictionary
        to a list and return the list.
    '''
    for k, v in structure_map.items():
        if k == map_type:
            for k2, v2 in v.items():
                for val in v2:
                    list_of_things.append(val)
    return list_of_things

def create_objects_lookup(a_list):
    '''
    Create a lookup table of potential structures for this map.
    
    Iterate over a_list, which is the list returned from create_list_of_structures
        and create new entries in a lookup table for each item in a_list
        that has a partner in globals().
    '''
    objects_lookup = {}
    for thing in a_list:
        if thing in globals().keys(): # globals().keys() returns key:value pairs of all global objects
            objects_lookup[thing] = globals()[thing]
    return objects_lookup

def instantiate_weights_dict(a_list):
    '''Create a dictionary where the keys are each item in a_list.'''
    # print("a_list: {}".format(a_list))
    return dict.fromkeys(a_list, 1)

def set_cols():
    '''Placeholder until GUI is created. Will pull from an input text field.'''
    pass
def set_rows():
    '''Placeholder until GUI is created. Will pull from an input text field.'''
    pass

# This should be a MapGrid specific method
def weighted_place():
    pass

num_cols = 20
num_rows = 20
num_buildings = 4
starting_tiles = 5
flora_density = "wooded"
capped_list = [] # list to keep track of structures that have reached their cap

if __name__ == "__main__":

    # instantiate our MapGrid object and pull the grid from it
    grid = MapGrid(num_rows, num_cols)
    map_grid = grid.grid

    # get a list of all structures we'll see on the map
    #  then create a lookup table of those structures
    struct_list = create_list_of_structures(type_of_map)
    objects_lookup = create_objects_lookup(struct_list)

    # initialize the field with starting_tiles number of structures
    grid.initialize_field(starting_tiles, struct_list, objects_lookup)

    # create the grid first
    for i in range(num_rows):
        for j in range(num_cols):
            # get weightings of all potential blocks that can be placed
            weights = instantiate_weights_dict(struct_list)
            # choose a random block to place based on weighting and place it
            grid.place_weighted(struct_list, capped_list, objects_lookup, weights, num_buildings, i, j)

    # paint the grid to a screen using the color of the structure at each map_grid point
    for i in range(num_rows):
        for j in range(num_cols):
            frame = tk.Frame(
                master = window,
                relief = tk.RAISED,
                borderwidth = 1
            )
            frame.grid(row=i, column=j)
            label = tk.Label(master=frame, bg=map_grid[i][j].color, width=4, height=2, text=map_grid[i][j])
            label.pack()

    window.mainloop()

