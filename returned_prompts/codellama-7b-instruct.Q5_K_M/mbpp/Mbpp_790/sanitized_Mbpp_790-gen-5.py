def even_position(my_list):
    return all([i % 2 == 0 for i in range(len(my_list)) if my_list[i] % 2 == 0])