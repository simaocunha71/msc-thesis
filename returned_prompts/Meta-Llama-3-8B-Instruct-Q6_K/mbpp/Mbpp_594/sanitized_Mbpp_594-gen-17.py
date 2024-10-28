def diff_even_odd(lst):
    even = None
    odd = None
    for num in lst:
        if num % 2 == 0:
            if even is None:
                even = num
        else:
            if odd is None:
                odd = num
    return even - odd