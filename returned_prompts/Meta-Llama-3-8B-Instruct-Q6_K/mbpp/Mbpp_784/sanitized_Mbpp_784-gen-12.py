def mul_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    if even and odd:
        return even[0] * odd[0]
    else:
        return 0