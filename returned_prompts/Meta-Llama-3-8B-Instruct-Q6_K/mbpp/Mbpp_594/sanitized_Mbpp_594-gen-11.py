def diff_even_odd(lst):
    even = next((x for x in lst if x % 2 == 0), None)
    odd = next((x for x in lst if x % 2 != 0), None)
    if even is None or odd is None:
        return None
    return abs(even - odd)