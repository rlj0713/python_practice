import itertools

def compare(number):
    string = str(number)
    ones = 0
    zeros = 0
    for i in string:
        if i == '1':
            ones += 1
        else:
            zeros += 1
    return(ones == zeros)


def increment_binary_digits(grid_width):
    count = 0
    for i in range (0, 2**(grid_width * 2)):
        binary = '{:040b}'.format(i)
        if compare(binary):
            count += 1
    print(count)

increment_binary_digits(20)