    min := math.Min(numbers...)
    max := math.Max(numbers...)
    return scale(numbers, min, max)
}

func scale(numbers []float64, min, max float64) []float64 {
    result := make([]float64, len(numbers))
    for i, number := range numbers {
        result[i] = (number - min) / (max - min)
    }
    return result
}



