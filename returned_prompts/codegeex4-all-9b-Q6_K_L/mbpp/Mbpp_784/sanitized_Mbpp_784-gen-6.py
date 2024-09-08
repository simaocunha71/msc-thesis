def mul_even_odd(lst):
    even = 1
    odd = 1
    for num in lst:
        if num % 2 == 0:
            even *= num
        else:
            odd *= num
    return even * odd