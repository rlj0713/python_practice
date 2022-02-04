import math
import random
from webbrowser import get

nums = open('matrix_test.txt', 'r+')
content = nums.read()
content_list = content.split(", ")

class Number:
    def __init__(self, row, column, value):
        self.row = int(row)
        self.column = int(column)
        self.value = int(value)
    
j = 1
c = 1
r = 1
for i in content_list:
    # globals() allows for a dynamic variable assignment
    globals()[f"v{c}{r}"] = Number(c, r, content_list[j - 1])
    if (r % 5) == 0:
        c += 1
    if r == 5:
        r = 1
    else:
        r += 1
    j += 1

#Format is 'v{row}{column}'
def check_number(object_name):
    print("row", object_name.row, "column", object_name.column, object_name.value)


def generate_route_list():
    route = [11]
    i = 11
    while len(route) < 9:
        to_add = random.choice([1, 10])
        i += to_add
        
        route.append(i)
    return route

generate_route_list()

# TO DO - Use the random generator to append routes to the master list
# Use a unique? comparison to populate the list without repeating.
list_of_all_possible_routes = []

while len(list_of_all_possible_routes) < 70:
    this_route = generate_route_list()
    
    if this_route not in list_of_all_possible_routes and this_route[-1] == 55:
        list_of_all_possible_routes.append(this_route)

# print(list_of_all_possible_routes)

def master_route_list_with_v(list_of_all_possible_routes):
    final_array = []
    for a in list_of_all_possible_routes:
        altered_array = []
        for i in a:
            altered_array.append('v' + str(i))
        final_array.append(altered_array)
    return(final_array)

all_routes = master_route_list_with_v(list_of_all_possible_routes)

array_of_sums = []
for r in all_routes:
    this_array_total = 0
    for i in r:
        this_array_total += eval(i).value
    array_of_sums.append(this_array_total)

# This successfully duplicates the example
print(sorted(array_of_sums)[0])