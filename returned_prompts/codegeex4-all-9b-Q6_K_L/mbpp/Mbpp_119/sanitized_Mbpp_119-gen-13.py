def search(nums: list) -> int:
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            return nums[i + 1]
    return nums[0]