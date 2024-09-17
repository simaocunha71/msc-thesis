def is_majority(nums, n, k):
    count = 0
    for num in nums:
        if num == k:
            count += 1
    if count > n // 2:
        return True
    else:
        return False