# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

import random

starting_point = [0, 0]
ending_point = [2, 2]

def random_index():
    return(random.randint(0, 1))


def generate_a_route():

    one_route = [[0, 0]]
    current_position = [0, 0]
    
    while current_position != [8, 8]:    
        current_position = one_route[len(one_route) - 1]

        if random_index() == 0:
            next_position = [current_position[0] + 1, current_position[1]]
        else:
            next_position = [current_position[0], current_position[1] + 1]

        if next_position[0] != 9 and next_position[1] != 9:
            one_route.append(next_position)

    return(one_route)
           

def generate_a_route_as_a_string():
    this_route = generate_a_route()
    string_route = ''
    for i in this_route:
        for j in i:
            y = str(j)
            string_route += y
    return(string_route)

array_of_all_routes = []

def add_a_route():
    new_route = generate_a_route_as_a_string()
    return new_route

while len(array_of_all_routes) < 12870:
    route_to_add = add_a_route()
    if array_of_all_routes.count(route_to_add) == 0:
        array_of_all_routes.append(route_to_add)


