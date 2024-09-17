def frequency(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count