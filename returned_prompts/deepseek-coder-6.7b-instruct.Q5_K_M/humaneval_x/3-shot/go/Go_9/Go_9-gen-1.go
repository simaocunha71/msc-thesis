    result := make([]int, len(numbers))
    max := math.MinInt64
    for i, num := range numbers {
        if num > max {
            max = num
        }
        result[i] = max
    }
    return result
}



