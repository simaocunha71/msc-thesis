    min_value := math.Min(numbers...)
    max_value := math.Max(numbers...)
    result := make([]float64, 0)

    for _, number := range numbers {
        result = append(result, (number - min_value) / (max_value - min_value))
    }
    return result
}



