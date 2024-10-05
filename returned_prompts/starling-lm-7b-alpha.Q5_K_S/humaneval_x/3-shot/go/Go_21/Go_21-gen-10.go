    min := math.Inf(1)
    max := 0.0

    for _, v := range numbers {
        if v < min {
            min = v
        }
        if v > max {
            max = v
        }
    }

    result := make([]float64, 0)
    for _, v := range numbers {
        result = append(result, (v - min) / (max - min))
    }
    return result
}



