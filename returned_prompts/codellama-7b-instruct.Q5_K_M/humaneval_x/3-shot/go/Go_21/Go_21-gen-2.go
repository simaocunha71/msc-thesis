    min := math.Min(numbers...)
    max := math.Max(numbers...)
    result := make([]float64, len(numbers))

    for i, n := range numbers {
        result[i] = (n-min)/(max-min)
    }
    return result
}



