    result := make([]int, 0)
    current_max := math.MinInt32

    for _, number := range numbers {
        if number > current_max {
            current_max = number
        }
        result = append(result, current_max)
    }
    return result
}



