    if len(arr) == 0 {
        return nil
    }

    sign := 1
    result := 0

    for _, v := range arr {
        if v > 0 {
            sign *= 1
        }else if v < 0 {
            sign *= -1
        }else {
            sign *= 0
        }
        result += v * int(math.Abs(float64(v)))
    }
    return result * sign
}



