def mul_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            even = num
        else:
            odd = num
        if even is not None and odd is not None:
            break
    return even * odd if even is not None and odd is not None else None