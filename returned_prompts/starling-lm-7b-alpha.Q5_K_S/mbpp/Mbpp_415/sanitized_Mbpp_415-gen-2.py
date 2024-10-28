def max_Product(nums):
    max_pair = (nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] > max_pair[0]:
            max_pair = (nums[i], max_pair[0])
        elif nums[i] > max_pair[1]:
            max_pair = (max_pair[0], nums[i])
    return max_pair