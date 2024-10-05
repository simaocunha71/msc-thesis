    min := math.Min(numbers...)
    max := math.Max(numbers...)
    result := make([]float64, len(numbers))
    for i := 0; i < len(numbers); i++ {
        result[i] = (numbers[i] - min) / (max - min)
    }
    return result
}



