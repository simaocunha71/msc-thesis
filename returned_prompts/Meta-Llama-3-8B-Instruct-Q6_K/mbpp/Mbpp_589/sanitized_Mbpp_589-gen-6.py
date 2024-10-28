def perfect_squares(start, end):
    perfect_squares_list = []
    for i in range(start, end + 1):
        sqrt = int(i ** 0.5)
        if sqrt * sqrt == i:
            perfect_squares_list.append(i)
    return perfect_squares_list