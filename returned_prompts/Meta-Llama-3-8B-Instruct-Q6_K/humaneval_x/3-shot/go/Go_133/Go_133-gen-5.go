    sum := 0
    for _, num := range lst {
        rounded := int(math.Ceil(num))
        sum += int(math.Pow(float64(rounded), 2))
    }
    return sum
}