    if n == 0:
        return [1, 3]
    elif n % 2 == 0:
        return [1, 3] + [1 + n / 2] * (n - 1)
    else:
        return [1, 3] + tri(n - 1) + tri(n - 2) + tri(n + 1)
