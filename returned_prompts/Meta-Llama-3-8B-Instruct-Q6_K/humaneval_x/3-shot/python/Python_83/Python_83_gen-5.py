    count = 0
    for num in range(10**(n-1), 10**n):
        if num % 10 == 1 or num // 10**n % 10 == 1:
            count += 1
    return count


