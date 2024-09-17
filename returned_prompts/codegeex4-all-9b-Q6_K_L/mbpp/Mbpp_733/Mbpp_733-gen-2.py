def find_first_occurrence(nums: list, num: int) -> int:
    for i in range(len(nums)):
        if nums[i] == num:
            return i
    return -1

