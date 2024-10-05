    var totalWater int
    for _, row := range grid {
        for _, cell := range row {
            if cell == 1 {
                totalWater += 1
            }
        }
    }
    var bucketCount int
    for totalWater > 0 {
        bucketCount++
        totalWater -= capacity
    }
    return bucketCount
}