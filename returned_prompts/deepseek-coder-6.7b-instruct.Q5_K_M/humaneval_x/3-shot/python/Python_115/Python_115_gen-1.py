    wells = []
    for row in grid:
        wells.extend(row)
    wells.sort(reverse=True)
    
    total_wells = len(wells)
    buckets = 0
    while wells and buckets < total_wells:
        if wells[-1] <= buckets * capacity:
            wells.pop()
            buckets += 1
        else:
            break
    return math.ceil(total_wells / capacity) - buckets

