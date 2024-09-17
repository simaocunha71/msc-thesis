def max_product(nums):
    cur_max, cur_min, res = float('-inf'), float('inf'), 0
    for num in nums:
        cur_max, cur_min = max(num, cur_max * num), min(num, cur_min * num)
        res = max(res, cur_max * cur_min)
    return res