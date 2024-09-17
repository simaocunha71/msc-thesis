def multiply_num(nums):
    product = 1
    for i in nums:
        product *= i
    return product / len(nums)