    sum := 0
    for i, v := range lst {
        if i % 3 == 0 {
            sum += int(math.Pow(float64(v), 2))
        } else if i % 4 == 0 && i % 3 != 0 {
            sum += int(math.Pow(float64(v), 3))
        } else {
            sum += v
        }
    }
    return sum
}