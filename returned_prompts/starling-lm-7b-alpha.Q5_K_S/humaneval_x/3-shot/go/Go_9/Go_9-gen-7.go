    result := make([]int, len(numbers))
    max := math.MinInt32
    for i, n := range numbers {
        if max < n {
            max = n
        }
        result[i] = max
    }
    return result
}



