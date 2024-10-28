def search(nums: list) -> int:
    return nums[len(nums) // 2] if len(nums) % 2 else nums[len(nums) // 2 - 1]