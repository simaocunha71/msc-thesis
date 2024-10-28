def check_Consecutive(nums: list) -> bool:
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)-1):
        if sorted_nums[i] + 1 != sorted_nums[i+1]:
            return False
    return True