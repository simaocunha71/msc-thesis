    max := math.MinInt64
    result := make([]int, len(numbers))

    for i, num := range numbers {
        if num > max {
            max = num
        }
        result[i] = max
    }

    return result
}



