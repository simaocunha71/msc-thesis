def max_subarray_product(nums: list) -> int:
    max_product = float('-inf')
    current_product = 1
    for num in nums:
        current_product *= num
        max_product = max(max_product, current_product)
        if current_product == 0:
            current_product = 1
    return max_product

