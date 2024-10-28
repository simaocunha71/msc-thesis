    def is_prime(n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    if a == 1:
        return False
    if a == 2:
        return False
    if a == 4:
        return False
    if a == 6:
        return False
    if a == 8:
        return False
    if a == 9:
        return False
    if a == 10:
        return False
    if a == 12:
        return False
    if a == 16:
        return False
    if a == 20:
        return False
    if a == 24:
        return False
    if a == 28:
        return False
    if a == 32:
        return False
    if a == 36:
        return False
    if a == 40:
        return False
    if a == 44:
        return False
    if a == 48:
        return False
    if a == 52:
        return False
    if a == 56:
        return False
    if a == 64:
        return False
    if a == 68:
        return False
    if a == 72:
        return False
    if a == 76:
        return False
    if a == 84:
        return False
    if a == 88:
        return False
    if a == 92:
        return False
    if a == 96:
        return False

    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0: