def cummulative_sum(t):
    res = 0
    for item in t:
        res += sum(item)
    return res