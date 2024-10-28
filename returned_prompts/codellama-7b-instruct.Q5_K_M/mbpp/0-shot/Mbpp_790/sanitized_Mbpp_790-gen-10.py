def even_position(my_list):
    # Check whether every even index contains even numbers
    for i in range(0, len(my_list), 2):
        if my_list[i] % 2 != 0:
            return False
    return True