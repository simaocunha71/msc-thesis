    min := math.Min(numbers...)
    max := math.Max(numbers...)
    result := make([]float64, len(numbers))
    for i, v := range numbers {
        result[i] = (v - min) / (max - min)
    }
    return result
}



