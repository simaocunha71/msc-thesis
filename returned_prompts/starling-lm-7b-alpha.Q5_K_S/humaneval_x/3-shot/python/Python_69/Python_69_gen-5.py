    d = {}
    for num in lst:
        if num not in d:
            d[num] = 0
        d[num] += 1
    max_num = max(lst)
    while d[max_num] < max_num:
        max_num -= 1
    return max_num if max_num > 0 else -1


