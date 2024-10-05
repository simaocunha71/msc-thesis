    max_fill = 0
    for row in grid:
        max_fill += math.ceil(sum(row) / capacity)
    return max_fill


