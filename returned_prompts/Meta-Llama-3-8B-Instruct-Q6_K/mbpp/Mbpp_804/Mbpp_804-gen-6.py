def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0
# Test the function
print(is_product_even([1,2,3]))  # Expected output: True
print(is_product_even([1,3,5]))  # Expected output: False
print(is_product_even([2,4,6]))  # Expected output: True
print(is_product_even([1,1,1]))  # Expected output: True
print(is_product_even([1,1]))  # Expected output: True
print(is_product_even([1]))  # Expected output: True
print(is_product_even([]))  # Expected output: True
print(is_product_even([2]))  # Expected output: True
print(is_product_even([4]))  # Expected output: True
print(is_product_even([6]))  # Expected output: True
print(is_product_even([8]))  # Expected output: True
print(is_product_even([0]))  # Expected output: True
print(is_product_even([0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # Expected output: True
print(is_product_even([0, 0, 0, 0, 0, 0, 0, 0,