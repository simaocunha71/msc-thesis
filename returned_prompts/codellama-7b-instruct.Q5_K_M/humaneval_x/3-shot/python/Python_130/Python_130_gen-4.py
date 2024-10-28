    if n == 1:
        return [1, 3, 2, 8]
    elif n % 2 == 0:
        return [1, 3, 2, 8] + tri(n - 1)
    else:
        return [1, 3, 2, 8] + tri(n - 1)
