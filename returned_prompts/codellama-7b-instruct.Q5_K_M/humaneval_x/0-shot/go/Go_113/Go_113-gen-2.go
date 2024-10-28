    for i, _ := range lst {
        for j, _ := range lst[i] {
            if i == j {
                goto A
            }
        }
    }

    return lst
}

