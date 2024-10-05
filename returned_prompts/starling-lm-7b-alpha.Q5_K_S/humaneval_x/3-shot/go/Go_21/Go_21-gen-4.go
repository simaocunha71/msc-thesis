    min_val := math.Inf(1)
    max_val := math.Inf(-1)
    for _, val := range numbers {
        if val < min_val {
            min_val = val
        }
        if val > max_val {
            max_val = val
        }
    }
    result := make([]float64, len(numbers))
    for i, val := range numbers {
        result[i] = (val - min_val) / (max_val - min_val)
    }
    return result
}




