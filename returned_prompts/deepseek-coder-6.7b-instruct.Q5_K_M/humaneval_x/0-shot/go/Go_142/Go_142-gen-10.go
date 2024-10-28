    sum := 0
    for index, value := range lst {
        switch {
        case index%3 == 0 && index%4 != 0:
            sum += int(math.Pow(float64(value), 2))
        case