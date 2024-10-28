
def cal_sum(n):
    if n <= 0:
        return 0
    else:
        return n + cal_sum(n-2)


