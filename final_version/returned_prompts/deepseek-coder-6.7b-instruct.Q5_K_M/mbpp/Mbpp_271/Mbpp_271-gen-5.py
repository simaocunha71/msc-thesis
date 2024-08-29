def even_Power_Sum(n):
    total = 0
    num = 2
    for i in range(n):
        total += num ** 5
        num += 2
    return total

assert even_Power_Sum(2) == 1056

