def mul_even_odd(lst):
    even_num = 1
    odd_num = 1
    for num in lst:
        if num % 2 == 0:
            even_num *= num
        else:
            odd_num *= num
    return even_num, odd_num