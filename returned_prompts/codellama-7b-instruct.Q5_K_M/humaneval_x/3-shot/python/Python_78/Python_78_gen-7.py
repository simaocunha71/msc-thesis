    count = 0
    for x in num:
        if int(x, 16) in [2, 3, 5, 7, 11, 13]:
            count += 1
    return count
