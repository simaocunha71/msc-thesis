    minimum = 1 << 31
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if minimum > sum(nums[i:j + 1]):
                minimum = sum(nums[i:j + 1])
    return minimum


