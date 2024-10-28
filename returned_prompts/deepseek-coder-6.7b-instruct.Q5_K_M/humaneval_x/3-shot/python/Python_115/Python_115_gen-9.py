    total_wells = sum(sum(row) for row in grid)
    return math.ceil(total_wells / capacity)


