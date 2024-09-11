def even_Power_Sum(n):
    total_sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total_sum += i ** 5
    return total_sum