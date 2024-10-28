def multiply_num(nums):
    product = 1
    for n in nums:
        product *= n
    return product / len(nums)