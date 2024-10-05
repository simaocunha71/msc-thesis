    def get_water_count(row, bucket_capacity):
        water_count = 0
        for cell in row:
            water_count += cell
        return math.ceil(water_count / bucket_capacity)

    total_buckets = 0
    for row in grid:
        total_buckets += get_water_count(row, capacity)

    return total_buckets

