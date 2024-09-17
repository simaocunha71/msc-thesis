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