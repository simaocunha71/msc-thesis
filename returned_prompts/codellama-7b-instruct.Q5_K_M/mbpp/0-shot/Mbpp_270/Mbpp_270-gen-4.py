def sum_even_and_even_index(my_list):
    return sum([element for index, element in enumerate(my_list) if index % 2 == 0 and element % 2 == 0])
