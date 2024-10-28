    max := math.MinInt64
    result := make([]int, len(numbers))

    for i, number := range numbers {
        if number > max {
            max = number
        }
        result[i] = max
    }

    return result
}



