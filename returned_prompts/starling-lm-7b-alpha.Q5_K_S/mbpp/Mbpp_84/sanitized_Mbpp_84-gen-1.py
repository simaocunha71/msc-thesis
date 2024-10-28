def sequence(n):
    if n < 4:
        return n
    else:
        return sequence(n - 1) + sequence(n - 2) + sequence(n - 3)