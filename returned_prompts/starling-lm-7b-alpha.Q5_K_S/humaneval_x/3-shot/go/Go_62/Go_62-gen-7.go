    result := make([]int, len(xs))
    result[0] = 0
    for i, x := range xs {
        if i == 0 {
            result[i] = 0
        } else {
            result[i] = x * i
        }
    }
    return result
}



