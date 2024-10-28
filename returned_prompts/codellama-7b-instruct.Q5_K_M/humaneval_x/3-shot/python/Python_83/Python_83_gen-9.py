    count = 0
    for i in range(10**n):
        s = str(i)
        if s[0] == '1' or s[-1] == '1':
            count += 1
    return count

