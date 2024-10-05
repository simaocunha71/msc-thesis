    if len(arr) == 0 {
        return nil
    }
    product_sign := 1
    for _, num := range arr {
        if num < 0 {
            product_sign *= -1
        } else if num == 0 {
            product_sign = 0
            break
        }
    }
    sum_magnitude := 0
    for _, num := range arr {
        sum_magnitude += int(math.Abs(float64(num)))
    }
    return product_sign * sum_magnitude
}

