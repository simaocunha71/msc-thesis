def mul_even_odd(lst):
    even_num = 1
    odd_num = 1
    for i in lst:
        if i % 2 == 0:
            even_num *= i
        else:
            odd_odd_num *= i
    return even_num, odd_num