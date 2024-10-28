def diff_even_odd(lst):
    even = [i for i in lst if i % 2 == 0]
    odd = [i for i in lst if i % 2 != 0]
    if not even or not odd:
        return None
    return even[0] - odd[0]