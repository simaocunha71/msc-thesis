    result := make([]int, len(numbers))
    current_max := math.MinInt64
    for i, n := range numbers {
        if n > current_max {
            current_max = n
        }
        result[i] = current_max
    }
    return result
}



