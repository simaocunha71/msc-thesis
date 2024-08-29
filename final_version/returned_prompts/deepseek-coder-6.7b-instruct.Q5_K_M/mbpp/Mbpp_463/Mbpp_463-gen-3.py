"""
The function works by iterating over the list and maintaining the maximum and minimum product so far.
The maximum product is necessary because a negative number multiplied by a negative number can become a large positive number.
On the other hand, the minimum product is necessary because a negative number multiplied by a large positive number can become a large negative number.

Then, at each position, we calculate the new maximum and minimum product by multiplying the current number with the current maximum and minimum product.

Finally, we return the maximum product found.

Here is the Python code for the above approach:
"""

def max_subarray_product(nums):
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))  # 112

"""
This function works by iterating over the list and maintaining the maximum and minimum product so far. 
At each position, it calculates the new maximum and minimum product by multiplying the current number with the current maximum and minimum product. 
Finally, it returns the maximum product found.
"""

"""
Time complexity: O(n), where n is the length of the array, because we iterate over the array once.
Space complexity: O(1), because we only use a constant amount of space to store the maximum, minimum, and result.
"""

"""
The function works by iterating over the list and maintaining the maximum and minimum product so far. 
On the other hand, the minimum product is necessary because a negative number multiplied by a large positive number can become a large negative number.

Then, at each position, we calculate the new maximum and minimum product by multiplying the current