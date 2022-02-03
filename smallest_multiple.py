all_numbers = list(range(0, 10000))
new_list = []
final_list = []

def is_prime(v):
    count = 0
    for x in range(0, v):
        if v % x == 0:
            count += 1
    if count > 2:
        print("false")
    else:
        print("true")

is_prime(4)


# for x in range(1, 10):
#     for i in all_numbers[::x]:
#         new_list.append(i)

# for i in all_numbers[::20]:
#     new_list.append(i)

# for x in all_numbers[::19]:
#     new_list.append(x)

# for x in all_numbers[::18]:
#     new_list.append(x)


# for j in new_list:
#     if new_list.count(j) == 10:
#         final_list.append(j)


# middle_index = len(final_list) // 10
# working_array = final_list[:middle_index]

# print(new_list)


