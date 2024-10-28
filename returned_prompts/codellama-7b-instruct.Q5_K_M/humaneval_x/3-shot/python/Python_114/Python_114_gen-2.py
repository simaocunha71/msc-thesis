    min_sum = 0
    for i in range(len(nums)):
        min_sum += nums[i]
        for j in range(i + 1, len(nums)):
            min_sum += nums[j]
            if min_sum < 0:
                min_sum = 0
            else:
                return min_sum


