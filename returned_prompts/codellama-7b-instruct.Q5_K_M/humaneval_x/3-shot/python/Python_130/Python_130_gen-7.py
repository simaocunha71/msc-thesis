    if n == 0:
        return [1]
    elif n % 2 == 0:
        return [1, 3] + [((n + 1) / 2) * (n / 2)]
    else:
        return [1, 3] + tri(n - 1) + tri(n - 2) + tri(n + 1)