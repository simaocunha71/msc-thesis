    if len(arr) == 0 {
        return nil
    }

    sum := 0
    prod := 1

    for _, v := range arr {
        if v > 0 {
            sum += int(math.Abs(float64(v)))
            prod *= 1
        } else if v < 0 {
            sum += int(math.Abs(float64(v)))
            prod *= -1
        } else {
            return 0
        }
    }

    return sum * prod
}



