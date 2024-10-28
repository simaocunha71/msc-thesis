def find_star_num(n):
    if n == 1:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total