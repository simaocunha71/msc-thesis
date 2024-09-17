def multiply_num(nums):
    res = 1
    for num in nums:
        res *= num
    return res / len(nums)