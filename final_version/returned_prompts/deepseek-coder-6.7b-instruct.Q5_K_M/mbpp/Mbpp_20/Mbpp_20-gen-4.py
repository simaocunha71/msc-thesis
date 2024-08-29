def is_woodall(n):
    digits = list(str(n))
    sum_of_digits = sum(map(int, digits))
    product_of_digits = 1
    for digit in digits:
        product_of_digits *= int(digit)
    return sum_of_digits == product_of_digits

assert is_woodall(383) == True
"""
