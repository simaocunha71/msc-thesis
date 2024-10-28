
def dif_Square(n: int):
    for i in range(1, n):
        if i * i - (n - i) * (n - i) == n:
            return True
    return False


