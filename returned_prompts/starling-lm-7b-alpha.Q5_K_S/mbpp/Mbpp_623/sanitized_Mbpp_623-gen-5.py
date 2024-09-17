def nth_nums(nums, n):
    res = []
    for num in nums:
        res.append(num ** n)
    return res
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]