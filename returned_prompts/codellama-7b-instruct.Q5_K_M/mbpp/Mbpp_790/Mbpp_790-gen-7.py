def even_position(my_list):
    return all(my_list[i] % 2 == 0 for i in range(0, len(my_list), 2))

# Note: all() is used to check if all elements in the list satisfies the condition
# range(0, len(my_list), 2) will give 0, 2, 4, ... 
# [i] % 2 == 0 will check if the element is even or not
