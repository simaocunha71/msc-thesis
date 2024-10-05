    result := make([]int, 0)

    max := math.MinInt64
    for _, n := range numbers{
        if n > max{
            max = n
        }
        result = append(result, max)
    }
    return result
}



