    min := math.Min(float64(math.MinInt64), math.Min(numbers...))
    max := math.Max(float64(math.MaxInt64), math.Max(numbers...))

    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / (max - min)
    }
    return result
}