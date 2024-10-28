def even_position(my_list):
    return all([i % 2 == 0 for i in range(len(my_list)) if my_list[i] % 2 == 0])

# Solution 2
def even_position(my_list):
    return all([my_list[i] % 2 == 0 for i in range(0, len(my_list), 2)])

# Solution 3
def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2))

# Solution 4
def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(len(my_list)) if i % 2 == 0)

# Solution 5
def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2) if my_list[i] % 2 == 0)

# Solution 6
def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2) if my_list[i] % 2 == 0)

# Solution 7
def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2) if my_list[i] % 2 == 0)

# Solution 8
def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2) if my_list[i] % 2 == 0)
