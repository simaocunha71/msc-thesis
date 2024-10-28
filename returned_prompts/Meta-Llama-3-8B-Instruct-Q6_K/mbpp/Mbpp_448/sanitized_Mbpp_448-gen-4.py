def cal_sum(n):
    perrin_nums = [3, 0, 2]
    for _ in range(3, n+1):
        perrin_nums.append(perrin_nums[-1] + perrin_nums[-2])
    return sum(perrin_nums[:n+1])  # sum of first n perrin numbers