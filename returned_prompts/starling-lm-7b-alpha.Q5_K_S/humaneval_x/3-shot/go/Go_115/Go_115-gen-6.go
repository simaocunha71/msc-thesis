    grid_size := len(grid) * len(grid[0])
    result := 0
    buckets := make([]int, grid_size)

    for i := 0; i < grid_size; i++ {
        buckets[i] += grid[i / len(grid[0])][i % len(grid[0])]
    }

    for buckets_size := capacity; ; buckets_size *= capacity {
        if buckets_size > grid_size {
            return result + grid_size / capacity
        }

        for i := 0; i < grid_size; i += buckets_size {
            if buckets[i] < buckets_size {
                continue
            }
            buckets[i] -= buckets_size
            for j := i + 1; j < i + buckets_size; j++ {
                buckets[j] += 1
            }
        }
        result += 1
    }

}



