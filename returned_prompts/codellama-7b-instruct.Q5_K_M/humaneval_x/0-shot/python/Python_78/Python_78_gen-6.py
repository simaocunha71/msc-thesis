
    num = str(num)
    count = 0
    for i in num:
        if i in '2357ABED':
            count += 1
    return count