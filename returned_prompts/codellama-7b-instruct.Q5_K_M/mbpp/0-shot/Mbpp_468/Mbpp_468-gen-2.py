"""
def max_product(arr):
    # find the maximum product of an increasing subsequence
    # the naive approach is to find the maximum product of all possible subsequence
    # but we can do better
    # the idea is to maintain the product of increasing subsequence
    # if we find a smaller number, we need to divide the product by it
    # and update the product
    # the time complexity is O(n) and space complexity is O(1)
    if len(arr) == 0:
        return 0
    product = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            product *= arr[i]
        else:
            product = arr[i]
    return product
"""