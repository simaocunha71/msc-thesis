    count = 0
    for num in range(10**(n-1), 10**n):
        if str(num).startswith('1') or str(num).endswith('1'):
            count += 1
    return count


