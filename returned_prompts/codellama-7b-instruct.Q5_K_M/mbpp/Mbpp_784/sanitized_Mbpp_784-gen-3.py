def mul_even_odd(my_list):
    even_product = 1
    odd_product = 1

    for i in my_list:
        if i % 2 == 0:
            even_product *= i
        else:
            odd_product *= i

    return even_product * odd_product