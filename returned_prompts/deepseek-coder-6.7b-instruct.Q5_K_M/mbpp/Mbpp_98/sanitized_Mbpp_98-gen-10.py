def multiply_num(num_list):
    total = 1
    for num in num_list:
        total *= num
    return total / len(num_list)