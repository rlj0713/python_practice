# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from itertools import permutations

set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_p = permutations(set)

list_of_all_permutations = []

for i in list(all_p):
    this_set = []
    for j in range(0, 10):
        this_set += i[j]
    list_of_all_permutations.append(this_set)

print(list_of_all_permutations[99999])