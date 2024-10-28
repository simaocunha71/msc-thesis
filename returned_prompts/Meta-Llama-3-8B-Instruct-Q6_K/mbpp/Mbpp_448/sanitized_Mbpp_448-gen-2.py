def cal_sum(n):
    if n == 0:
        return 0
    perrin_nums = [0, 0, 2]
    for i in range(3, n + 1):
        perrin_nums.append(perrin_nums[i - 1] + perrin_nums[i - 2] - perrin_nums[i - 3])
    return sum(perrin_nums) - 2