"""
Write a function to find the maximum product subarray of the given array.
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
"""
def maxSubArrayProduct(arr):
    if not arr:
        return 1
    max_so_far = 0
    for i, val in enumerate(arr[::-1]):
        curr_max = max_so_far * (i + 1)
        max_so_far = max(curr_max, arr[i]) * (i + 1)

    return max_so_far
