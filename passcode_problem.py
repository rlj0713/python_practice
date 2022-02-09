
# Codes are imported and converted to integers in a list
def import_codes():
    content = open('p079_keylog.txt', 'r+').read()
    codes_csv = content.split(',')
    code_list = []

    for i in codes_csv:
        code_list.append(int(i))
    return code_list


c = import_codes()

p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
p9 = []
p10 = []

for i in c:
    first_digit = int(str(i)[0])
    last_digit = int(str(i)[2])
    if first_digit not in p1:
        p1.append(first_digit)
    if last_digit not in p10:
        p10.append(last_digit)

p1.sort()
p10.sort()

print(p1)
print(p10)