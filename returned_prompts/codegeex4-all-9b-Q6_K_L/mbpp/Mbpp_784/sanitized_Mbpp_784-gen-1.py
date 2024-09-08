def mul_even_odd(lst):
    even = 1
    odd = 1
    for i in lst:
        if i % 2 == 0:
            even = even * i
        else:
            odd = odd * i
    return even * odd