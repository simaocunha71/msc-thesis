def diff_even_odd(lst):
    first_even = None
    first_odd = None
    for num in lst:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    if first_even is not None and first_odd is not None:
        return first_even - first_odd
    else:
        return None