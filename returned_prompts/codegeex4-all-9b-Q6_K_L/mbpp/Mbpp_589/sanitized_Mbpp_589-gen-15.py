def perfect_squares(start, end):
    result = []
    for i in range(start, end+1):
        if int(math.sqrt(i))**2 == i:
            result.append(i)
    return result