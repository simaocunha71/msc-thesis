    if n == 1:
        return [1]

    if n % 2 == 0:
        return [n] + make_a_pile(n + 1)

    return [n] + make_a_pile(n + 2)
