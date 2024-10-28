    sum := 0
    for i, val := range lst {
        if i % 3 == 0 {
            sum += int(math.Pow(float64(val), 2))
        } else if i % 4 == 0 && i % 3 != 0 {
            sum += int(math.Pow(float64(val), 3))
        } else {
            sum += val
        }
    }
    return sum
}