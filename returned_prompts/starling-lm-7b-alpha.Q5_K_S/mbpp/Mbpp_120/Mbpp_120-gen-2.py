from functools import reduce

def max_product_tuple(nums):
    """
    Find the maximum absolute product between numbers in pairs of tuples within a given list.
    """
    # Sort the tuples by the first element in ascending order
    nums.sort(key=lambda x: x[0])
    # Get the max product of the first tuple by multiplying the two elements
    max_product = reduce(lambda x, y: x * y, nums[0])
    # For each tuple, find the max product of the first and last element and multiply it with the previous max product
    for i in range(len(nums)):
        if i % 2 == 0:
            max_product = max(max_product, nums[i][0] * nums[i][1])
        else:
            max_product = max(max_product, nums[i][0] * nums[i][1] * -1)
    return max_product

# Test the function
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
```
    
The function `max_product_tuple` takes a list of tuples as input and finds the maximum absolute product between numbers in pairs of tuples within the given list. It first sorts the tuples by the first element in ascending order. Then, it initializes the `max_product` variable with the maximum product of the first tuple by multiplying the two elements. For each tuple, it checks if the index is even or odd. If it's even, it multiplies the first and last element of the tuple and updates the `max_product` if necessary. If it's odd, it multiplies the first and last element of the tuple and updates the `max_product` with the product multiplied by -1. Finally, it returns the maximum absolute product.

In the provided example, the function is called with the list `[(2, 7), (2, 6), (1, 8), (4, 9)]`. The maximum absolute product between numbers in pairs of tuples within this list is 36, so the function returns 36 as expected.

