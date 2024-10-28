
def diff_even_odd(lst):
    even = next((i for i in lst if i % 2 == 0), None)
    odd = next((i for i in lst if i % 2 != 0), None)
    return even - odd if even and odd else None

