def sum_even_and_even_index(my_list):
    sum = 0
    for index, value in enumerate(my_list):
        if index % 2 == 0 and value % 2 == 0:
            sum += value
    return sum