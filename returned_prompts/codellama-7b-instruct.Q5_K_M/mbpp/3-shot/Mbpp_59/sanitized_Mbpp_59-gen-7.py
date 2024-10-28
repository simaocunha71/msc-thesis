def is_octagonal(n):
    sqrt = int(n**0.5)
    if sqrt**2 == n:
        return n
    for i in range(1, sqrt):
        if (n - i**2 - 1) % 2 == 0:
            return (n - i**2 - 1) // 2
    return None