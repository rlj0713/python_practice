# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# sudo apt update
# sudo apt install python3-pip
# pip install num2words

from num2words import num2words
import re

print(num2words(115))

# def sum_this_number(x):