def closest_num(n):
    if n <= 0:
        return None
    for i in range(n-1, 0, -1):
        if i < n:
            return i