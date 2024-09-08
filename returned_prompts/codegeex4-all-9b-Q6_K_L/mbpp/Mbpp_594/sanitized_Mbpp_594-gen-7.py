def diff_even_odd(lst):
    first_even = None
    first_odd = None
    for num in lst:
        if num % 2 == 0:
            if first_even is None:
                first_even = num
        else:
            if first_odd is None:
                first_odd = num
    if first_even is not None and first_odd is not None:
        return first_even - first_odd
    return None