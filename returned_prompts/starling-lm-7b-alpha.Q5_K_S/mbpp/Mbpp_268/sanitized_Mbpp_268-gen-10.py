def find_star_num(n):
    if n < 0:
        return 0
    else:
        return n * (n + 1) // 2