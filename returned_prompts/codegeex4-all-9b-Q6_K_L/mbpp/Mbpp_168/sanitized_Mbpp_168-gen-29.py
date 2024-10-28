def frequency(nums: list, num: int) -> int:
    count = 0
    for i in nums:
        if i == num:
            count += 1
    return count