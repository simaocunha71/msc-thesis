def mul_even_odd(lst):
    even_num = None
    odd_num = None
    for num in lst:
        if num % 2 == 0:
            even_num = num
        else:
            odd_num = num
        if even_num is not None and odd_num is not None:
            break
    return even_num * odd_num if even_num is not None and odd_num is not None else None