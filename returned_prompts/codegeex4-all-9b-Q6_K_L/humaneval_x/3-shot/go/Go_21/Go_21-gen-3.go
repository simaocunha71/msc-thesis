    min := math.Inf(1)
    max := math.Inf(-1)

    for _, n := range numbers{
        if n < min{
            min = n
        }
        if n > max{
            max = n
        }
    }

    result := make([]float64, 0)
    for _, n := range numbers{
        result = append(result, (n-min)/(max-min))
    }

    return result
}



