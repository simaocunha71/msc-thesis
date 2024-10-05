    min_number := min(numbers)
    max_number := max(numbers)
    range_number := max_number - min_number

    result := make([]float64, len(numbers))

    for i, number := range numbers {
        result[i] = (number - min_number) / range_number
    }
    return result
}



