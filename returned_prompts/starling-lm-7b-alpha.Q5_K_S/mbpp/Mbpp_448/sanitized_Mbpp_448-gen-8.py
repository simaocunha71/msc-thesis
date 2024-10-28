from itertools import accumulate
def cal_sum(n):
    perrin = [1] + list(accumulate(perrin))
    return sum(perrin[:n+1])