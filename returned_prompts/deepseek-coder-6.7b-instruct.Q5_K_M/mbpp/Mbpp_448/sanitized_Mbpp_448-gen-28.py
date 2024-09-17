def cal_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        perrin = [0, 0, 1]
        for i in range(3, n + 1):
            perrin.append(perrin[i - 1] + perrin[i - 2] + perrin[i - 3])
        return sum(perrin)