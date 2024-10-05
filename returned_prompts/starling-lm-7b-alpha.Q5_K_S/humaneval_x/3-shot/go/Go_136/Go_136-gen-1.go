    if len(lst) == 0 {
        return [2]interface{}{nil, nil}
    }
    min := math.MaxInt32
    max := math.MinInt32
    for i := range lst {
        if lst[i] > max {
            max = lst[i]
        }
        if lst[i] < min {
            min = lst[i]
        }
    }
    return [2]interface{}{max, min}
}



