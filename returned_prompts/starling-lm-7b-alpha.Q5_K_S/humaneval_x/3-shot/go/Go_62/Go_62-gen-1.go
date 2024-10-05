    result := make([]int, len(xs))
    for i, x := range xs {
        if i == 0 {
            continue
        }

        result[i-1] = x * i
    }
    return result
}



