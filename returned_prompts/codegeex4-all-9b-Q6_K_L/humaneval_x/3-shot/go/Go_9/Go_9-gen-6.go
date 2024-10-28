    maxes := make([]int, 0)

    max := math.MinInt64
    for _, n := range numbers {
        if n > max {
            max = n
        }
        maxes = append(maxes, max)
    }

    return maxes
}



