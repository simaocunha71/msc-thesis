def dif_Square(n):
    # check if n is a perfect square
    root = int(n**0.5)
    if root**2 == n:
        return True
    else:
        return False