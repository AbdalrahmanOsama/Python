my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for i in range(len(my_list)):
    is_unique = True
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            is_unique = False
            break
    if is_unique:
        unique_list.append(my_list[i])

print("The list with unique elements only:")
print(unique_list)
