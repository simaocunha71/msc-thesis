def search(nums: list):
    return nums[nums.index(nums[0]) ^ nums.index(nums[-1])]

