def dif_Square(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            if n // i == i:
                return True
            elif (n // i - i) % 2 == 0:
                return True
        i += 1
    return False