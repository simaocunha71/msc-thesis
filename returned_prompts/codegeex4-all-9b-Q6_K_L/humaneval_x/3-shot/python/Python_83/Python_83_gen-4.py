    count = 0
    for num in range(10**(n-1), 10**n):
        if str(num)[0] == '1' or str(num)[-1] == '1':
            count += 1
    return count

