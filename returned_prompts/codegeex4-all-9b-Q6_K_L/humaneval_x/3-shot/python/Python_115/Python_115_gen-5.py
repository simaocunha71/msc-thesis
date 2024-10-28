    def count_buckets(wells, capacity):
        total_buckets = 0
        for well in wells:
            total_buckets += math.ceil(sum(well) / capacity)
        return total_buckets

    def reduce_wells(wells, capacity):
        for i in range(len(wells)):
            while sum(wells[i]) >= capacity:
                wells[i] = [x - capacity for x in wells[i]]
                total_buckets += 1
        return wells

    total_buckets = count_buckets(grid, capacity)
    wells = reduce_wells(grid, capacity)

    while sum(wells[0]) > 0:
        wells = reduce_wells(wells, capacity)

    return total_buckets

