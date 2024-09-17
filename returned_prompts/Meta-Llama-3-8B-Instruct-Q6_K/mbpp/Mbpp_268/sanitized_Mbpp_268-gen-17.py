def find_star_num(n):
    total = 0
    for i in range(1, n+1):
        total += i * i
    return total