def cal_sum(n):
    total_sum = 0
    running_sum = 0

    for i in range(n + 1):
        total_sum += running_sum
        running_sum += (2 * i + 1)

    return total_sum