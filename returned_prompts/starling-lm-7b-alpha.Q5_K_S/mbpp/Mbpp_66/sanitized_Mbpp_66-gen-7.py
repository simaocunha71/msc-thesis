def pos_count(nums):
    cnt = 0
    for i in nums:
        if i > 0:
            cnt += 1
    return cnt