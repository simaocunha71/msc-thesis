    total := 0
    for _, row := range grid {
        for _, water := range row {
            if water == 1 {
                total += 1
            }
        }
    }
    return total / capacity
}

