# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

import random

starting_point = [0, 0]
ending_point = [2, 2]

def random_index():
    return(random.randint(0, 1))


def next_position(last_position, square_size):
    while last_position != ending_point:
        random_num = random_index()
        if last_position[random_num] < square_size and last_position[random_num] != last_position:
            last_position[random_num] += 1
            return(last_position)
        
this_route = [[0, 0]]

print(next_position(this_route[len(this_route) - 1], 2))

