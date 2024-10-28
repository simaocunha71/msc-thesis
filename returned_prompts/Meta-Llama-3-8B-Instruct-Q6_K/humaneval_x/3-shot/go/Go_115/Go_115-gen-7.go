    var total int
    for _, row := range grid {
        for _, val := range row {
            total += val
        }
    }
    return total / capacity
}