    max_water := 0
    for _, row := range grid {
        for _, col := range row {
            max_water += col
        }
    }
    return max_water / capacity
}

