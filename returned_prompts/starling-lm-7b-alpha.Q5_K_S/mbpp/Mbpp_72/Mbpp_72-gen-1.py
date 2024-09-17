
def dif_Square(n: int) -> bool:
    for i in range(1,n):
        if (i ** 2) - (n ** 2) == 0:
            return True
    return False


