def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        nums = [1, 1]
        for i in range(2, n):
            nums.append(nums[i-2] + nums[i-1])
        return nums[-1]