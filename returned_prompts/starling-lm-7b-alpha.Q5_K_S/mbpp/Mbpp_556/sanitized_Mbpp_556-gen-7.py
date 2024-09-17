def find_Odd_Pair(nums, n):
    odd = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if (nums[i]^nums[j]) & 1:
                odd += 1
    return odd