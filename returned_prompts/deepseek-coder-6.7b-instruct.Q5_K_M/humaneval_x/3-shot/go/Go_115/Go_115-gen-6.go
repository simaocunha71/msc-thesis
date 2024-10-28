    var waterCount int
    for _, row := range grid {
        for _, well := range row {
            waterCount += well
        }
    }

    return int(math.Ceil(float64(waterCount) / float64(capacity)))
}



