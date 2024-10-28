
def max_subarray_product(nums):
    if not nums:
        return 0

    max_prod, min_prod, result = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)

    return result


