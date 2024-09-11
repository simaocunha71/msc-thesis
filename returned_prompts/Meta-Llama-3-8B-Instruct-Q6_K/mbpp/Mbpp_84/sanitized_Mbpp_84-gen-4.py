def sequence(n):
    if n <= 2:
        return 1
    else:
        return sequence(n-1) + sequence(n-2)