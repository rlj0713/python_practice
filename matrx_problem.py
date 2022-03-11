import math
import random
from webbrowser import get

nums = open('p081_matrix.txt', 'r+')
content = nums.read()
content_list = content.split(",")

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
    # If then block evalutaes number of digits and adds leading 0 if the location is a single digit coordiante
    if len(str(c)) <= 1 and len(str(r)) <= 1:
        globals()[f"v{c}0{r}"] = Number(c, r, content_list[j - 1])
    elif len(str(c)) <= 1 and len(str(r)) > 1:
        globals()[f"v{c}{r}"] = Number(c, r, content_list[j - 1])
    elif len(str(c)) > 1 and len(str(r)) <= 1:
        globals()[f"v{c}0{r}"] = Number(c, r, content_list[j - 1])
    else:
        globals()[f"v{c}{r}"] = Number(c, r, content_list[j - 1])


    if (r % 80) == 0:
        c += 1
    if r == 80:
        r = 1
    else:
        r += 1
    j += 1

# Format is 'v{row}{column}'
def check_number(object_name):
    print("row", object_name.row, "column", object_name.column, object_name.value)

# There is potentially a problem.  What is v111, is that row 11, column 1 or row 1 column 11 
# I need to store 1 as 01 to solve this
# This appears to be working now, v0101 returns 4445
# check_number(v0101)

def generate_route_list():
    # Starting coordinates are represented as an integer here 11 in the example
    # 11 no longer works, now we need 0101
    route = [101]
    i = 101
    while len(route) < 159:
        if len(str(i)) <= 3:
            to_add = random.choice([1, 100])
        else:
            to_add = random.choice([1, 100])
        
        i += to_add
        route.append(i)
    return route


generate_route_list()

# TO DO - Use the random generator to append routes to the master list
# Use a unique? comparison to populate the list without repeating.
list_of_all_possible_routes = []

#There happen to be 70 total routes in a 5 x 5 matrix.  Need to calculate for 80 x 80
def obtain_a_record():
    while len(list_of_all_possible_routes) < 1000:
        this_route = generate_route_list()
        
        if this_route not in list_of_all_possible_routes and this_route[-1] == 8080:
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
    return(sorted(array_of_sums)[0])


newest_record = 664678

def one_trial(old_record):
    result = obtain_a_record()
    if result < old_record:
        print(result)
    else:
        print(i)

for i in range(100):
    one_trial(newest_record)