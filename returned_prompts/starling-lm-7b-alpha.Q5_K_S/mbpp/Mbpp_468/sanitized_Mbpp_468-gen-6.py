def max_product(nums):
    max_product = 1
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            max_product *= nums[left]
            left += 1
        else:
            max_product *= nums[right]
            right -= 1

    return max_product