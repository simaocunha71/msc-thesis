def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = float('inf')

    for num in nums:
        max_product, min_product = max(max_product * num, min_product * num, num), min(max_product * num, min_product * num, num)
        max_product = max(max_product, min_product)

    return max_product