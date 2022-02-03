import csv
import string

with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    names_array = list(reader)[0]

sorted_names = sorted(names_array)

current_score = 0
a_string = string.ascii_uppercase
alphabet_list = list(a_string)

dictionary_with_scores = {}

i = 1
for letter in alphabet_list:
    dictionary_with_scores[letter] = i
    i += 1

def score_this_name(index, name_string):
    score = 0
    for letter in name_string:
        score += dictionary_with_scores[letter]
    score = score * index
    return score

def score_the_list(array_of_names):
    total = 0

    j = 1
    for name in array_of_names:
        total += score_this_name(j, name)
        j += 1
    return total


print(score_the_list(sorted_names))