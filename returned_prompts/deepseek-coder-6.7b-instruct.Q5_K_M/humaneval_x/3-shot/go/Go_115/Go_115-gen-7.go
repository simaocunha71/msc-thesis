    total_water :=0
    for _, row := range grid {
        for _, well := range row {
            total_water += well
        }
    }
    return int(math.Ceil(float64(total_water)/float64(capacity)))
}



