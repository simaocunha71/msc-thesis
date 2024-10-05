    total_wells = sum([sum(row) for row in grid])
    buckets = math.ceil(total_wells / capacity)
    return buckets

