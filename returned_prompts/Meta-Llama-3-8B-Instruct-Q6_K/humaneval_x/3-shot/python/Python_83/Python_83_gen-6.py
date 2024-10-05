    count = 0
    for i in range(10**(n-1), 10**n):
        if i // 10**(n-1) == 1 or i % 10**(n-1) == 1:
            count += 1
    return count


