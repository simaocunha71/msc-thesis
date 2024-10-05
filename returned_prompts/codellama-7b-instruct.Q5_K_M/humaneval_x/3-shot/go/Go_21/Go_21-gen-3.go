    min := math.Min(numbers...)
    max := math.Max(numbers...)
    range := max - min

    result := make([]float64, len(numbers))
    for i, v := range numbers {
        result[i] = (v - min) / range
    }
    return result
}



