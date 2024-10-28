def cal_sum(n):
    if n < 2:
        return 0
    else:
        return n + cal_sum(n - 1)