def max_product(nums: list) -> int:
    n = len(nums)
    max_product = 0
    for i in range(n):
        for j in range(i, n):
            max_product = max(max_product, nums[i] * nums[j])
    return max_product

