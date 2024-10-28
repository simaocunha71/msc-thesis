def diff_even_odd(lst):
    even = next((num for num in lst if num % 2 == 0), None)
    odd = next((num for num in lst if num % 2 != 0), None)
    if even is None or odd is None:
        return None
    return even - odd