    total = 0
    for row in grid:
        for col in row:
            total += col

    return math.ceil(total / capacity)

