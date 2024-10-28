    max_val := numbers[0]
    min_val := numbers[0]
    result := make([]float64, 0)

    for _, n := range numbers {
        if n > max_val {
            max_val = n
        }
        if n < min_val {
            min_val = n
        }
    }

    for _, n := range numbers {
        result = append(result, (n - min_val) / (max_val - min_val))
    }
    return result
}



