def mul_even_odd(lst):
    even = [num for num in lst if num % 2 == 0]
    odd = [num for num in lst if num % 2 != 0]
    if len(even) == 0 or len(odd) == 0:
        return None
    return even[0] * odd[0]