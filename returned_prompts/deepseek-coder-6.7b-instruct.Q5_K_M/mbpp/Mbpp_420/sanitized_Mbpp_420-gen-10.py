def cube_Sum(n):
    total = 0
    even_num = 2
    for _ in range(n):
        total += even_num ** 3
        even_num += 2
    return total