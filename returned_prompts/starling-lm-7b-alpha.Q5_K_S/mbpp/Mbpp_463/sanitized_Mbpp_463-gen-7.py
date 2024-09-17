def max_subarray_product(nums):
    min_end = float('inf')
    max_so_far = float('-inf')
    max_product = float('-inf')

    for num in nums:
        min_end = min(min_end, num)
        max_so_far = max(max_so_far, num)
        max_product = max(max_product, max_so_far - min_end)

    return max_product