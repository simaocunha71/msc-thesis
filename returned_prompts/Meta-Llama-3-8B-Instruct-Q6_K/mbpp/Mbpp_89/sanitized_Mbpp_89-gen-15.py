def closest_num(n):
    if n == 0:
        return -1
    for i in range(n-1, -1, -1):
        if i < n:
            return i
    return -1