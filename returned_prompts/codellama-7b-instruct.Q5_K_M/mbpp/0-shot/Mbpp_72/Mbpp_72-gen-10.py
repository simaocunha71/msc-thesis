def dif_Square(num):
    # Check if num is a perfect square
    root = int(num ** 0.5)
    if root ** 2 == num:
        return True

    # Check if (num + 1) is a perfect square
    root = int((num + 1) ** 0.5)
    if (root + 1) ** 2 == num + 1:
        return True

    return False
