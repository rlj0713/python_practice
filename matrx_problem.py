import math

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

print(route1)


