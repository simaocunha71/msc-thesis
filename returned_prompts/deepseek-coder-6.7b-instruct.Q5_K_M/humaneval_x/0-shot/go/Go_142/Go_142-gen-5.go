    sum := 0
    for idx, val := range lst {
        switch {
        case idx % 3 == 0:
            sum += int(math.Pow(float64(val), 2))
        case idx % 4 == 0:
            sum += int(math.Pow(float64(val), 3))
        default:
            sum += val
        }
    }
    return sum
}


