def next_Perfect_Square(num):
    # Find the next perfect square
    root = num ** 0.5
    root = int(root)
    root += 1
    root **= 2
    return root