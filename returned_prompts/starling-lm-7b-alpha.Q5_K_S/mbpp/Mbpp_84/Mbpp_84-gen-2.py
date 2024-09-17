
def sequence(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return sequence(n // 2) + 1
    else:
        return sequence(n - 1) + 1


