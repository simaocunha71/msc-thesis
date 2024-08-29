def perfect_squares(start: int, end: int):
    return [i * i for i in range(start, end + 1) if int(i * i) <= end]