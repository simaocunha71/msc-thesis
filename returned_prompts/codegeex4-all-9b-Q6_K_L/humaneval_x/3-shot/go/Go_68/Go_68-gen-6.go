    min_val := math.MaxInt64
    min_idx := -1
    for i, v := range arr {
        if v % 2 == 0 && v < min_val {
            min_val = v
            min_idx = i
        }
    }
    if min_val == math.MaxInt64 {
        return []int{}
    }
    return []int{min_val, min_idx}
}

