def find_star_num(n):
    if n == 1:
        return 1
    else:
        return 2 * find_star_num(n - 1) + 1