
def cal_sum(n: int) -> int:
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return cal_sum(n-1) + n * cal_sum(n-2)


