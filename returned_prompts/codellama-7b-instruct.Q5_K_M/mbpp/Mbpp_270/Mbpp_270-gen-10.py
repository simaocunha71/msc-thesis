def sum_even_and_even_index(my_list):
    sum = 0
    for index, item in enumerate(my_list):
        if index % 2 == 0 and item % 2 == 0:
            sum += item
    return sum
