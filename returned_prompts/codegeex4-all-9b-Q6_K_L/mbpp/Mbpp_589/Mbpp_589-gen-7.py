def perfect_squares(start, end):
    squares = []
    for num in range(start, end+1):
        if num ** 0.5 == int(num ** 0.5):
            squares.append(num)
    return squares

