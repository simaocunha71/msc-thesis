def first_odd(nums: list) -> int:
    for num in nums:
        if num % 2 != 0:
            return num

