def is_majority(nums: list, n: int, num: int) -> bool:
    count = 0
    for i in range(n):
        if nums[i] == num:
            count += 1
    return count > n // 2