def mul_even_odd(lst):
    for num in lst:
        if num % 2 == 0:
            even = num
        else:
            odd = num
    return even * odd