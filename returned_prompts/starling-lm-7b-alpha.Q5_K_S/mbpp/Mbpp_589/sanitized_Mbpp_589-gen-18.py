def perfect_squares(start, end):
    return [x * x for x in range(start, end + 1) if x * x <= end]