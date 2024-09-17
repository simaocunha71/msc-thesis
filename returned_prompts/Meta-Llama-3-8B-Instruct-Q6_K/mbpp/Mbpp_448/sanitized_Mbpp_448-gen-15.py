def cal_sum(n):
    if n <= 2:
        return 3
    perrin = [3, 0, 2]
    for i in range(3, n+1):
        perrin.append(perrin[i-1] + perrin[i-2] + perrin[i-3])
    return sum(perrin)