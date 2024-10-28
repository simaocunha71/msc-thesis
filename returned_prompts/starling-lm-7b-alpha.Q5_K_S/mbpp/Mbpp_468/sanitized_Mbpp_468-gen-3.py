def max_product(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    if len(nums) == 3:
        return max(nums[0] * nums[1] * nums[2], max(nums[0], nums[1]), max(nums[0], nums[2]))
    inc_prev = [nums[0]]
    inc_curr = [nums[1]]
    for i in range(2, len(nums)):
        if nums[i] > inc_prev[len(inc_prev) - 1]:
            inc_curr.append(nums[i])
        else:
            while inc_prev[len(inc_prev) - 1] > nums[i]:
                inc_prev.pop()
            inc_prev.append(nums[i])
            inc_curr.append(max(inc_prev[len(inc_prev) - 1], inc_curr[len(inc_curr) - 1]))
    return max(inc_curr)