def sum_negativenum(lst):
    res = 0
    for x in lst:
        if x < 0:
            res += x
    return res