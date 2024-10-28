    min := math.Min(float64(numbers[0]), math.Min(float64(numbers[1:]...)))
    max := math.Max(float64(numbers[0]), math.Max(float64(numbers[1:]...)))
    return make([]float64, len(numbers))
    for i, num := range numbers {
        scaled := (num - min) / (max - min)
        result[i] = scaled
    }
    return result
}