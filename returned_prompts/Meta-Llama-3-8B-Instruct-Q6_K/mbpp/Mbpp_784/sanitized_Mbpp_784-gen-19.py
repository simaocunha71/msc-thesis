def mul_even_odd(lst):
    if not lst:
        return None
    even = [i for i in lst if i % 2 == 0]
    odd = [i for i in lst if i % 2 != 0]
    if even and odd:
        return even[0] * odd[0]
    return None