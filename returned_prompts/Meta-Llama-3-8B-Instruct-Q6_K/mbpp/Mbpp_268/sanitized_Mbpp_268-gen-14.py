def find_star_num(n):
    total = 0
    for i in range(n):
        total += int('1' * (i + 1))
    return total