    count = 0
    for row in grid:
        count += math.ceil(sum(row) / capacity)
    return count

