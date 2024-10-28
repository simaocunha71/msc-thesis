    min := math.Inf(1)
    max := math.Inf(-1)
    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }

    result := make([]float64, len(numbers))
    for i, num := range numbers {
        result[i] = (num - min) / (max - min)
    }
    return result
}

