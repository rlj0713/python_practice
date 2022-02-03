import random

peter_die = [1, 2, 3, 4]
colin_die = [1, 2, 3, 4, 5, 6]

peter_array = []
colin_array = []

for x in range(10000000):
    peter_array.append(random.choice(peter_die))
    colin_array.append(random.choice(colin_die))


p_score = 0
c_score = 0
draw_score = 0

i = 0
for n in peter_array:
    if n > colin_array[0]:
        p_score += 1
    elif n == colin_array[0]:
        draw_score += 1
    else:
        c_score += 1
    i += 1


print(p_score)
