def cal_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        perrin_nums = [3, 2]
        for _ in range(2, n):
            perrin_nums.append(perrin_nums[-1] + perrin_nums[-2])
        return sum(perrin_nums)