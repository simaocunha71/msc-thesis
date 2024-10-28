    count = 0
    for row in grid:
        for well in row:
            count += well
    return -(-count // capacity)


