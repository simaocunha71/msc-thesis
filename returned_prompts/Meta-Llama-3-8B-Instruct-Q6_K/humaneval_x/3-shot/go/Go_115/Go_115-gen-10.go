    var total_water int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                total_water++
            }
        }
    }
    return total_water / capacity
}