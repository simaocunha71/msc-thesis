def search(nums: list) -> int:
    for i in range(len(nums)):
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]