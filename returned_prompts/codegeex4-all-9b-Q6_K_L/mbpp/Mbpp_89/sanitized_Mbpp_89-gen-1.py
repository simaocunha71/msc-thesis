def closest_num(n):
    if n == 0:
        return None
    if n % 10 != 0:
        return n // 10 * 10 + 9
    else:
        return closest_num(n // 10) * 10 + 9