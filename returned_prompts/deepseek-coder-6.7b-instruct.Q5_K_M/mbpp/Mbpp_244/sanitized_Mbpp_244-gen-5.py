def next_Perfect_Square(n):
    # find square root of n
    sqrt = n ** 0.5

    # if sqrt is not integer then n is not a perfect square
    if sqrt != int(sqrt):
        return "Number is not a perfect square"

    # else increment the square root and return the square of it
    sqrt += 1
    return sqrt * sqrt