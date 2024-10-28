    min := math.Min(numbers...)
    max := math.Max(numbers...)
    result := make([]float64, 0, len(numbers))
    for _, n := range numbers {
        result = append(result, (n - min) / (max - min))
    }
    return result
}



