    if len(arr) == 0 {
        return nil
    }
    product := 1
    sum := 0
    for _, num := range arr {
        if num > 0 {
            product *= 1
        } else if num < 0 {
            product *= -1
        }
        sum += math.Abs(float64(num))
    }
    return sum * float64(product)
}