def max_Product(nums):
    if (len(nums) == 1):
        return (nums[0], None)
    elif (len(nums) == 2):
        return (nums[0], nums[1])
    else:
        max_num = -float('inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j):
                    if (nums[i] * nums[j] > max_num):
                        max_num = nums[i] * nums[j]
                        max_i = i
                        max_j = j
        return (nums[max_i], nums[max_j])