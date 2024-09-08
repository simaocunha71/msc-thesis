def max_Product(nums):
    max_product = 0
    num1 = num2 = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]*nums[j] > max_product:
                max_product = nums[i]*nums[j]
                num1 = nums[i]
                num2 = nums[j]
    return (num1, num2)