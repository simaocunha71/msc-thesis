    count = 0
    for row in grid:
        count += sum(row)
    return (count + capacity - 1) // capacity


