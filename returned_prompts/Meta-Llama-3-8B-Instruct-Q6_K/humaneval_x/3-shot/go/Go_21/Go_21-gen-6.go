    minVal := math.MinFloat64
    maxVal := math.MaxFloat64

    for _, val := range numbers {
        if val < minVal {
            minVal = val
        }
        if val > maxVal {
            maxVal = val
        }
    }

    result := make([]float64, len(numbers))
    for i, val := range numbers {
        result[i] = (val - minVal) / (maxVal - minVal)
    }
    return result
}