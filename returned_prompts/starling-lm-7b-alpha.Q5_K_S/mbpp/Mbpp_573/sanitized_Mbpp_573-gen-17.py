def unique_product(nums):
    nums.sort()
    unique_nums = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            unique_nums.append(nums[i])
    product = 1
    for i in range(len(unique_nums)):
        product *= unique_nums[i]
    return product