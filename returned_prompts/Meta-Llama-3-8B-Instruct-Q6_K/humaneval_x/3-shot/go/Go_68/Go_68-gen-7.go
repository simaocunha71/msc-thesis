    var result []int
    var min_val int
    var min_index int

    for i, val := range arr {
        if val % 2 == 0 {
            if result == nil || val < min_val {
                min_val = val
                min_index = i
                result = []int{min_val, min_index}
            }
        }
    }
    return result
}