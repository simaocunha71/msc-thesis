def sum_even_and_even_index(my_list):
    return sum(num for index, num in enumerate(my_list) if index % 2 == 0 and num % 2 == 0)



