    if len(arr) == 0 {
        return nil
    }
    prod := 1
    sum := 0
    for _, v := range arr {
        if v > 0 {
            prod *= 1
            sum += float64(v)
        } else if v < 0 {
            prod *= -1
            sum -= float64(v)
        } else {
            prod *= 0
        }
    }
    return prod * sum
}