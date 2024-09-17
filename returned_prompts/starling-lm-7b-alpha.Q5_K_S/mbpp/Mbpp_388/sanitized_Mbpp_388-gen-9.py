def highest_Power_of_2(n):
    if n == 0:
        return 0
    while n % 2 == 0:
        n = n/2
    return n