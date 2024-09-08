def frequency(lst, num):
    count = 0
    for n in lst:
        if n == num:
            count += 1
    return count