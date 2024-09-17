def last(nums: list, val: int) -> int:
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == val:
            return i
    return -1

