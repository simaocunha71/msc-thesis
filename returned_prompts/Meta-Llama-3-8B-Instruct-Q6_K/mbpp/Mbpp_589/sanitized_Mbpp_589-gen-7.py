def perfect_squares(start, end):
    result = []
    for i in range(start, end+1):
        root = int(i**0.5)
        if root**2 == i:
            result.append(i)
    return result