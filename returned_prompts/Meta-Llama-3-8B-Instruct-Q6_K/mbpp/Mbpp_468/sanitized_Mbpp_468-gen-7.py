def max_product(nums):
    max_product = [num for num in nums]
    min_product = [num for num in nums]
    for i in range(1, len(nums)):
        max_product[i] = max(nums[i], max_product[i-1] * nums[i])
        min_product[i] = min(nums[i], min_product[i-1] * nums[i])
    return max(max_product)  # or return max(max_product) if you want the maximum product