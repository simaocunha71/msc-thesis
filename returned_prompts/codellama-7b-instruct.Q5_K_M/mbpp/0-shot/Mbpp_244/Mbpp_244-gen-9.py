def next_Perfect_Square(num):
    # Find next perfect square
    root = int(num ** 0.5)
    return root * root if root ** 2 == num else (root + 1) ** 2
