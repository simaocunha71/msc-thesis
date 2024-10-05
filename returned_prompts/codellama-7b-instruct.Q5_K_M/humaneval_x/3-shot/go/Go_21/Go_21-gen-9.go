    min := math.Min(numbers[0], math.Min(numbers[1:]...))
    max := math.Max(numbers[0], math.Max(numbers[1:]...))
    result := make([]float64, len(numbers))
    for i, n := range numbers {
        result[i] = (n - min) / (max - min)
    }
    return result
}



