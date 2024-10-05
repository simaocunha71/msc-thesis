    result := make([]int, 0)
    current := n
    for current > 1 {
        if current % 2 == 1 {
            result = append(result, current)
        }
        if current % 2 == 0 {
            current = current / 2
        } else {
            current = 3 * current + 1
        }
    }
    sort.Slice(result, func(i, j int) bool { return result[i] < result[j] })
    return result
}



