    min := math.Min(float64(1e9), math.MinFloat64)
    max := math.Max(float64(-1e9), math.MaxFloat64)

    for _, num := range numbers {
        min = math.Min(min, num)
        max = math.Max(max, num)
    }

    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / (max - min)
    }
    return result
}