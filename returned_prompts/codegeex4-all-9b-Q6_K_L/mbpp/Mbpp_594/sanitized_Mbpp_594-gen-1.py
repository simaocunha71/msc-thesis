def diff_even_odd(lst):
    even = next((i for i in lst if i % 2 == 0), None)
    odd = next((i for i in lst if i % 2 == 1), None)
    if even is None or odd is None:
        return None
    else:
        return abs(even - odd)