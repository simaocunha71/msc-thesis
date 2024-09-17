def diff_even_odd(lst):
    for num in lst:
        if num % 2 == 0: 
            even = num
        elif num % 2 != 0:
            odd = num
    return even - odd