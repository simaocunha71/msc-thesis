    result := make([]int, 0)
    min := math.MaxInt32
    max := math.MinInt32

    for _, v := range lst {
        if v < min {
            min = v
        }
        if v > max {
            max = v
        }
    }
    result = append(result, min)

    sort.Slice(lst, func(i, j int) bool {
        return lst[i] > lst[j]
    })
    for _, v := range lst {
        if v != max {
            result = append(result, v)
        }
    }

    return result
}