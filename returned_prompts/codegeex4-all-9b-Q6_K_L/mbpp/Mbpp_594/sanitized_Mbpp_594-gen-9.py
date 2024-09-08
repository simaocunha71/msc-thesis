def diff_even_odd(lst):
    first_even = next((x for x in lst if x % 2 == 0), None)
    first_odd = next((x for x in lst if x % 2 != 0), None)
    if first_even is not None and first_odd is not None:
        return first_even - first_odd
    return None