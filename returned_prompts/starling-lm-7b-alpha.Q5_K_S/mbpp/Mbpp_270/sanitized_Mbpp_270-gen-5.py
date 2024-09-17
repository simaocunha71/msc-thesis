def sum_even_and_even_index(input_list):
    summ = 0
    for i in range(0, len(input_list), 2):
        if input_list[i] % 2 == 0:
            summ += input_list[i]
    return summ