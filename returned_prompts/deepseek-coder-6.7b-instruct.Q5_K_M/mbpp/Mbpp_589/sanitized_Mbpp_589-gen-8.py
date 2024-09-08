def perfect_squares(start, end):
    return [i * i for i in range(start, end+1) if int(i**0.5)**2 == i * i]