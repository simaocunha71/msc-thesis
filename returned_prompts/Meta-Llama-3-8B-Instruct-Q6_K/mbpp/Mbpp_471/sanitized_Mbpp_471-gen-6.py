def find_remainder(nums, n):
    res = 1
    for i in nums:
        res = (res * i) % n
    return res