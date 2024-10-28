def even_Power_Sum(n):
    if n < 1:
        return 0
    else:
        return sum([i ** 5 for i in range(2, 2 * n + 1)])