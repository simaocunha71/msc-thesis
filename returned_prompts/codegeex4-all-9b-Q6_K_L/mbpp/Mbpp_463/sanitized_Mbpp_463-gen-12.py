def max_subarray_product(nums: list) -> int:
    max_product = nums[0]
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product > max_product:
                max_product = product
    return max_product