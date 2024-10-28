def mul_even_odd(lst):
    even_numbers = [x for x in lst if x % 2 == 0]
    odd_numbers = [x for x in lst if x % 2 != 0]
    if even_numbers and odd_numbers:
        return even_numbers[0] * odd_numbers[0]
    else:
        return 0