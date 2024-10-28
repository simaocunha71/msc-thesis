def cal_sum(n):
    perrin = [3, 0, 2]
    if n <= 2:
        return perrin[n]
    for i in range(3, n+1):
        perrin.append(perrin[i-1] + perrin[i-2] - perrin[i-3])
    return sum(perrin)