def perfect_squares(start, end):
    result = []
    for i in range(start, end + 1):
        if i ** 0.5 == int(i ** 0.5):
            result.append(i)
    return result