def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = float('inf')
    for num in nums:
        max_product = max(max_product * num, num)
        min_product = min(min_product * num, num)
    return max(0, max_product)