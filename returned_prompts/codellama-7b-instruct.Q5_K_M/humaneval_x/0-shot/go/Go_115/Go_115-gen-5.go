    for _, row := range grid {
        if len(row) == 0 {
            continue A
        }
        for i := 0; i < len(row); i++ {
            if row[i] == 0 {
                continue A
            }
        }
    }

    for _, row := range grid {
        if len(row) == 0 {
            continue A
        }
        for i := 0; i < len(row); i++ {
            if row[i] == 1 {
                continue A
            }
        }
    }

    return 0
}
