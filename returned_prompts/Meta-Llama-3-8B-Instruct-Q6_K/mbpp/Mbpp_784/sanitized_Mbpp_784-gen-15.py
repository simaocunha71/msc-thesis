def mul_even_odd(lst):
    even_num = next((i for i in lst if i % 2 == 0), None)
    odd_num = next((i for i in lst if i % 2 != 0), None)
    if even_num is None or odd_num is None:
        return 0
    return even_num * odd_num