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

check_number(v11)
check_number(v51)
check_number(v23)
check_number(v43)
check_number(v55)


route1 = v11.value + v21.value + v31.value + v41.value + v51.value + v52.value + v53.value + v54.value + v55.value
route2 = v11.value + v21.value + v31.value + v41.value + v42.value + v52.value + v53.value + v54.value + v55.value
route3 = v11.value + v21.value + v31.value + v41.value + v42.value + v43.value + v53.value + v54.value + v55.value

def generate_route_list():
    route = [11]
    i = 11
    while len(route) < 9:
        to_add = random.choice([1, 10])
        i += to_add
        
        route.append(i)
    print(route)
    return route

print(route1)
print(route2)
print(route3)

generate_route_list()

# TO DO - Use the random generator to append routes to the master list
# Use a unique? comparison to populate the list without repeating.
list_of_all_possible_routes = []
