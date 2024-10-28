def dif_Square(n):
    i = 1
    while i * i <= n:
        if n == i * i:
            return True
        elif n > i * i:
            if n % (2 * i) == 0:
                return True
            else:
                i += 1
        else:
            i += 1
    return False