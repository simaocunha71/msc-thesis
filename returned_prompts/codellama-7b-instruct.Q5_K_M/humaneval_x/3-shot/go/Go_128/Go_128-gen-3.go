    if len(arr) == 0 {
        return nil
    }

    var result float64 = 1
    var product float64 = 1
    for _, num := range arr {
        if num == 0 {
            result = 0
            continue
        }
        if num < 0 {
            result *= -1
        }
        product *= math.Abs(float64(num))
    }

    return result * product
}



