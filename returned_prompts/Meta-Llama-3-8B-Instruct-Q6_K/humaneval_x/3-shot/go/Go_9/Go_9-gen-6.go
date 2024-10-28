    result := make([]int, 0)
    maxSoFar := math.MinInt32

    for _, num := range numbers {
        if num > maxSoFar {
            maxSoFar = num
        }
        result = append(result, maxSoFar)
    }
    return result
}