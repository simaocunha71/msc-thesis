def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    for i in lst:
        if i % 2 == 0:
            even_product *= i
        else:
            odd_product *= i
    return even_product, odd_product

even_product, odd_product = mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8])
print(even_product, odd_product)

# Expected output:
# 96 384

# 