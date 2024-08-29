def perfect_squares(start: int, end: int):
    return [i**2 for i in range(int(start**0.5), int(end**0.5)+1)]