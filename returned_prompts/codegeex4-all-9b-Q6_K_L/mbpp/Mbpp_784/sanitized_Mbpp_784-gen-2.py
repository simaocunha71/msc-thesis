def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    for i, num in enumerate(lst):
        if i % 2 == 0:
            even_product *= num
        else:
            odd_product *= num
    return even_product * odd_product