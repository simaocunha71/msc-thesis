    min_value := numbers[0]
    max_value := numbers[0]

    for _, value := range numbers {
        if value < min_value {
            min_value = value
        } else if value > max_value {
            max_value = value
        }
    }

    result := make([]float64, len(numbers))
    for i := 0; i < len(numbers); i++ {
        result[i] = (numbers[i] - min_value) / (max_value - min_value)
    }
    return result
}



