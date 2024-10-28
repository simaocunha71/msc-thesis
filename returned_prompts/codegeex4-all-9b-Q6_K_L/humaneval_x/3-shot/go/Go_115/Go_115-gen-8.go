    total := 0
    for _, row := range grid {
        for _, elem := range row {
            if elem == 1 {
                total += 1
            }
        }
    }
    return total / capacity
}

