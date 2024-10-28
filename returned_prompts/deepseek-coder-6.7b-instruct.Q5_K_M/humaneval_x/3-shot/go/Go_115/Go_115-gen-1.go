    var total int
    for _, row := range grid {
        for _, well := range row {
            total += well
        }
    }
    return int(math.Ceil(float64(total) / float64(capacity)))
}


