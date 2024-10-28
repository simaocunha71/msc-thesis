    min := math.Min(float64(1e10), math.Min(numbers...))
    max := math.Max(float64(-1e10), math.Max(numbers...))
    scale := 1.0 / (max - min)
    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) * scale
    }
    return result
}