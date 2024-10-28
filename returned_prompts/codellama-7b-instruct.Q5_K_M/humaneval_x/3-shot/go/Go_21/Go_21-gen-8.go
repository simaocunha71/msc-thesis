    min_value := math.Min(numbers...)
    max_value := math.Max(numbers...)
    result := make([]float64, 0)

    for _, n := range numbers {
        result = append(result, (n - min_value) / (max_value - min_value))
    }
    return result
}



