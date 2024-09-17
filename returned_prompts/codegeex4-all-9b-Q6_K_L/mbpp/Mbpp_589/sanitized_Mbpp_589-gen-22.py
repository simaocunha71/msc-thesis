def perfect_squares(start: int, end: int) -> list:
    return [i for i in range(start, end+1) if i**0.5 == int(i**0.5)]