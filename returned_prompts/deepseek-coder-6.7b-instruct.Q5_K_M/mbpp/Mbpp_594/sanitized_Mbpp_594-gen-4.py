def diff_even_odd(lst):
    first_even = next((i for i in lst if i % 2 == 0), None)
    first_odd = next((i for i in lst if i % 2 != 0), None)
    return first_even - first_odd if first_even and first_odd else None