    max_number := math.MinInt64
    result := make([]int, len(numbers))
    for i, number := range numbers {
        if number > max_number {
            max_number = number
        }
        result[i] = max_number
    }
    return result
}



