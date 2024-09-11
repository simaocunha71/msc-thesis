def is_product_even(nums):
    return all(num % 2 == 0 for num in nums)


def is_product_even(nums):
    if len(nums)==0:
        return True
    else:
        return nums[0] % 2 == 0 and is_product_even(nums[1:])

assert is_product_even([1,2,3])


"""
The function is_product_even(nums) checks whether the product of the numbers in the list nums is even or not.

In the function is_product_even(nums), the function all is used to check whether all the elements in the list nums satisfy the condition num % 2 == 0. If all the elements satisfy this condition, the function returns True; otherwise, it returns False.

In the function is_product_even(nums), the function all is used to check whether the first number in the list nums is even (num % 2 == 0) and the product of the remaining numbers in the list is even (is_product_even(nums[1:])). If both conditions are satisfied, the function returns True; otherwise, it returns False.
"""

def is_product_even(nums):
    if len(nums)==0:
        return True
    else:
        return nums[0] % 2 == 0 and is_product_even(nums[1:])


assert is_product_even([1,2,3])

# The function is_product_even(nums) checks whether the product of the numbers in the list nums is even or not.
# The function all is used to check whether all the elements in the list nums satisfy the condition num % 2 == 0. If all the elements satisfy this condition, the function returns True; otherwise, it returns False.
# The function is_product_even(nums) checks whether the first number in the list nums is even (num % 2 == 0) and the product of the remaining numbers in the list is even (is_product_even(nums[1:])). If both conditions are satisfied, the function returns True; otherwise, it returns False.
