def cal_sum(n):
    perrin = [3, 0, 2]
    for i in range(3, n):
        perrin.append(perrin[i-1] + perrin[i-2] - perrin[i-3])
    return sum(perrin[:n+1])