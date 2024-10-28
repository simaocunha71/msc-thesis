def mul_even_odd(my_list):
    product = 1
    for i, num in enumerate(my_list):
        if i % 2 == 0:
            product *= num
        else:
            product *= num
    return product