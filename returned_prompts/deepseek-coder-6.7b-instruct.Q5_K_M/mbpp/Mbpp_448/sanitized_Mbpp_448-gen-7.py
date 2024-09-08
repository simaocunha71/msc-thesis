def cal_sum(n):
    if n < 0:
        return "Input should be positive integer."
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        perrin = [0, 1, 2]
        for i in range(3, n+1):
            perrin.append(perrin[i-2] + perrin[i-3])
        return sum(perrin)