    sum := 0
    for _, num := range lst {
        ceiling := math.Ceil(num)
        sum += int(math.Pow(float64(int(ceiling)), 2))
    }
    return sum
}