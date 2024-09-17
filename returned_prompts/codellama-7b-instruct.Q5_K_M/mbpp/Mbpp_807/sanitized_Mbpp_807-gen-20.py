def first_odd(nums):
    for num in nums:
        if num % 2 == 1:
            return num
    return None