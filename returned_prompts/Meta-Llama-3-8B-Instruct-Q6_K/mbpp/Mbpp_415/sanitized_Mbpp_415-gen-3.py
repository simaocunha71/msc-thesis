def max_Product(nums):
    nums.sort()
    return (nums[-1], nums[-2]) if nums[-1] * nums[-2] > nums[0] * nums[-1] else (nums[0], nums[1])  # O(n log n)