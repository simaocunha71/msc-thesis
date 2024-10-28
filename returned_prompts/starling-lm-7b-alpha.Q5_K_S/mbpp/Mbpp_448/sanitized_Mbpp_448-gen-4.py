def cal_sum(n):
    nums = [0] * (n+1)
    nums[0] = 1
    nums[1] = 2
    for i in range(2,n+1):
        nums[i] = nums[i-1] + i * (i+1)
    return sum(nums)