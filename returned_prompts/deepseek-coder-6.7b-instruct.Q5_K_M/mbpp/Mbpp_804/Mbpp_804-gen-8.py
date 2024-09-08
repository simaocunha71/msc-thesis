
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0

print(is_product_even([1,2,3])) # False
print(is_product_even([1,2,3,4])) # True

"""
Explanation:
We initialize a variable `product` to 1. Then we iterate through each number in the given list and multiply the `product` by the current number. After we have gone through all numbers in the list, we check if the `product` is divisible by 2. If it is, then the product is even and the function returns True, otherwise it returns False.
"""

# 5.

