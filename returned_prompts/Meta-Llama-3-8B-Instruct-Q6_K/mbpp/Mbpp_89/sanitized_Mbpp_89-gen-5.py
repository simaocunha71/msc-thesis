def closest_num(n):
    for i in range(n-1, -1, -1):
        if i != n:
            return i
    return None