    total_wells := 0
    for _, row := range grid {
        for _, well := range row {
            total_wells += well
        }
    }

    return int(math.Ceil(float64(total_wells) / float64(capacity)))
}



