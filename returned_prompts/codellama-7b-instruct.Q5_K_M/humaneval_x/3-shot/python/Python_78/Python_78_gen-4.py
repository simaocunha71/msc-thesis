    num = str(num)
    count = 0
    for i in range(len(num)):
        if num[i] in 'ABED':
            count += 1

    return count


