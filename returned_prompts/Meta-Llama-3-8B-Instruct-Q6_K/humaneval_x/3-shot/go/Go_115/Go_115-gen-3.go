    var total int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                total += 1
            }
        }
    }
    return total / capacity + (total % capacity > 0)
}