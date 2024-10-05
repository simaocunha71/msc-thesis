    result := make([]int, 0)
    current_max := math.MinInt32

    for _, n := range numbers {
        if n > current_max {
            current_max = n
        }
        result = append(result, current_max)
    }
    return result
}



