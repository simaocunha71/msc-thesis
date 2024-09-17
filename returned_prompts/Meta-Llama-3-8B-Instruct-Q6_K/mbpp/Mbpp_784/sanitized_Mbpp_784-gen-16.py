def mul_even_odd(lst):
    for num in lst:
        if num % 2 == 0:
            even_num = num
            break
    for num in lst:
        if num % 2 != 0:
            odd_num = num
            break
    return even_num * odd_num