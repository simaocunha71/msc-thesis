
def is_product_even(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product % 2 == 0

assert is_product_even([1,2,3]) == False

# Problem 2
