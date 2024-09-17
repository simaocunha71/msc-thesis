def max_product_tuple(nums):
    max_product = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            max_product = max(max_product, abs(nums[i][0]*nums[j][0]), abs(nums[i][0]*nums[j][1]), abs(nums[i][1]*nums[j][0]), abs(nums[i][1]*nums[j][1]), nums[i][0]*nums[j][1], nums[i][1]*nums[j][0])
    return max_product