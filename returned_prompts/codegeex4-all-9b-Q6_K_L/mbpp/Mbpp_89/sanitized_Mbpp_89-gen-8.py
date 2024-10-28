def closest_num(n):
    if n <= 0:
        return None
    if n % 10 == 0:
        return n - 1
    else:
        return n - n % 10 + 9