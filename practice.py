
def addMultiples(x, y, max_number):

    total = 0

    for i in range(max_number):
        if i % x == 0 or i % y == 0:
            total += i

    print(total)

addMultiples(3, 5, 1000)