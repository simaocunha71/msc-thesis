def even_Power_Sum(n):
    total = 0
    even_num = 2
    for _ in range(n):
        total += even_num ** 5
        even_num += 2
    return total