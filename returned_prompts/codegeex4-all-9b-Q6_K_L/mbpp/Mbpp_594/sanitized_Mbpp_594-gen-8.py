def diff_even_odd(lst):
    for i in lst:
        if i % 2 == 0:
            first_even = i
            break
    for i in lst:
        if i % 2 != 0:
            first_odd = i
            break
    return first_even - first_odd