    var count int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                count += capacity
            }
        }
    }
    return count
}