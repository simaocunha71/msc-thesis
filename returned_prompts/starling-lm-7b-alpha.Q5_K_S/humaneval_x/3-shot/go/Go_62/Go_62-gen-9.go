    result := make([]int, len(xs)-1)
    for i, v := range xs {
        if i == 0 {
            result[i] = v
        } else {
            result[i-1] += v * i
        }
    }
    return result
}



