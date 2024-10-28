def max_Product(nums):
    max_product = (nums[0], nums[1])
    for i in range(2, len(nums)):
        if nums[i] * max_product[0] > max_product[1] * nums[i]:
            max_product = (max_product[0], nums[i])
        elif nums[i] * max_product[1] > max_product[0] * nums[i]:
            max_product = (nums[i], max_product[1])
    return max_product