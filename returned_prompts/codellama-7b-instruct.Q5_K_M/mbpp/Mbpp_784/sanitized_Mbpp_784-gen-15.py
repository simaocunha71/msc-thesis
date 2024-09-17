def mul_even_odd(my_list):
    even = 1
    odd = 1
    for i in my_list:
        if i % 2 == 0:
            even *= i
        else:
            odd *= i
    return even*odd