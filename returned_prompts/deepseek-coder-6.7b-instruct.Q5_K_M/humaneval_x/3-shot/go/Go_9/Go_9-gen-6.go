    result := make([]int, len(numbers))
    current_max  := math.MinInt64
    for i, num := range numbers {
        if num > current_max {
            current_max = num
        }
        result[i] = current_max
    }
    return result
}



