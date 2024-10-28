def multiple_to_single(nums: list) -> int:
    result = 0
    for num in nums:
        result = result * 100 + num
    return result

