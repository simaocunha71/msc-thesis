def even_Power_Sum(n):
    total = 0
    for i in range(n):
        total += (2 * i + 2) ** 5
    return total