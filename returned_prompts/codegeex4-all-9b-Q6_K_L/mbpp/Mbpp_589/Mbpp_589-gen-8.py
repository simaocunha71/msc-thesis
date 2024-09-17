def perfect_squares(start: int, end: int) -> list:
    return [i*i for i in range(start, end+1) if i*i <= end]

