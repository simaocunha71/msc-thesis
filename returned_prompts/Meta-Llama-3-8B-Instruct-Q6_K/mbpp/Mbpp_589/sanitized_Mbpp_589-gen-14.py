def perfect_squares(start, end):
    perfect_squares = []
    for i in range(start, end+1):
        square_root = int(i ** 0.5)
        if square_root ** 2 == i:
            perfect_squares.append(i)
    return perfect_squares