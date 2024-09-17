def sum_even_and_even_index(my_list):
    return sum([my_list[i] for i in range(len(my_list)) if i % 2 == 0])