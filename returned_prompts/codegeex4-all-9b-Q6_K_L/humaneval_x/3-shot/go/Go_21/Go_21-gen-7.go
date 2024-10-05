    min := math.Inf(1)
    max := math.Inf(-1)

    for _, number := range numbers {
        if number < min {
            min = number
        }
        if number > max {
            max = number
        }
    }

    result := make([]float64, 0, len(numbers))
    for _, number := range numbers {
        result = append(result, (number-min)/(max-min))
    }

    return result
}



