
def pancake_sort(nums: list) -> list:
    for i in range(len(nums)):
        max_num = max(nums[:i+1])
        index = nums[:i+1].index(max_num)
        nums.insert(0, nums[i+index])
        del nums[i+index+1]
    return nums


