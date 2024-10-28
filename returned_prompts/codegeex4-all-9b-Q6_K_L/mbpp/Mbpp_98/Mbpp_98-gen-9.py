def multiply_num(nums: list) -> float:
    total = 1
    for num in nums:
        total *= num
    return total / len(nums)