def sequence(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    else:
        return sequence(n-1) + sequence(n-2)