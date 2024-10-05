    # sort the sides by length
    a, b, c = sorted([a, b, c])

    # check if the sum of the squares of the two smaller sides is equal to the square of the largest side
    return a**2 + b**2 == c**2


