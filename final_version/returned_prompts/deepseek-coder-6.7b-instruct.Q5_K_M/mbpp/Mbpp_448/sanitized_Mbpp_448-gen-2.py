def cal_sum(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        perrin = [0, 1, 2]
        for i in range(3, n):
            perrin.append(perrin[i-2] + perrin[i-3])
        return sum(perrin)