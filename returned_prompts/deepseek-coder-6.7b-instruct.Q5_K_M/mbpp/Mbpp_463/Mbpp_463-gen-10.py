
def max_subarray_product(nums):
    if not nums:
        return 0
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        temp_max = max(current, max_so_far*current, min_so_far*current)
        min_so_far = min(current, max_so_far*current, min_so_far*current)
        max_so_far = temp_max
        result = max(result, max_so_far)
    return result


