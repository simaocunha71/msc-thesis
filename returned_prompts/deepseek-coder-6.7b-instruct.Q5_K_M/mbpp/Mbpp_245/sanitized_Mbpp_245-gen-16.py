def max_sum(lst):
    l = len(lst)
    if l < 3:
        return max(lst)
    inc = [0]*l
    dec = [0]*l
    max_sum = [0]*l
    inc[0] = lst[0]
    dec[-1] = lst[-1]
    for i in range(1, l):
        inc[i] = max(inc[i-1], lst[i]) if inc[i-1] > lst[i] else lst[i]
    for i in range(l-2, -1, -1):
        dec[i] = max(dec[i+1], lst[i]) if dec[i+1] > lst[i] else lst[i]
    for i in range(l):
        max_sum[i] = inc[i] + dec[i] - lst[i]
    return max(max_sum)