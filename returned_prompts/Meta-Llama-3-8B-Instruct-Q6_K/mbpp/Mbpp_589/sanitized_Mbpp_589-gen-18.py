def perfect_squares(start, end):
    result = []
    for i in range(int(start**0.5), int(end**0.5) + 1):
        if i**2 >= start and i**2 <= end:
            result.append(i**2)
    return result