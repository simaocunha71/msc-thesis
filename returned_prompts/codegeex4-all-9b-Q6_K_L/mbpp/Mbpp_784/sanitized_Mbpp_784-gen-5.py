def mul_even_odd(lst):
    even_products = 1
    odd_products = 1
    for i in range(len(lst)):
        if i % 2 == 0:
            even_products *= lst[i]
        else:
            odd_products *= lst[i]
    return even_products * odd_products