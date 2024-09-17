
def perfect_squares(start, end):
    return [x**2 for x in range(start, end+1) if x**2 >= start and x**2 <= end]


