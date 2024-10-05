    if len(arr) == 0 {
        return nil
    }

    sign := 1
    sum := 0
    for _, num := range arr {
        if num < 0 {
            sign *= -1
        }
        sum += math.Abs(float64(num))
    }

    return sign * sum
}