import itertools

def compare(number, grid_width):
    string = str(number)
    ones = 0
    for i in string:
        if i == '1':
            ones += 1
    return(ones == grid_width)


def increment_binary_digits(grid_width):
    count = 0
    for i in range (0, 2**(grid_width * 2)):
        binary = '{:012b}'.format(i)
        if compare(binary, grid_width):
            count += 1
            if count % 10000 == 0:
                print(count)
    print(count)

increment_binary_digits(6)

# n = 41
 
# for i in range(1, n+1):
#     for j in range(0, n-i+1):
#         print(' ', end='')
 
#     # first element is always 1
#     C = 1
#     for j in range(1, i+1):
 
#         # first value in a line is always 1
#         print(' ', C, sep='', end='')
 
#         # using Binomial Coefficient
#         C = C * (i - j) // j
#     print()