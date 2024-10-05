    result := make([]int, len(xs))
    result[0] = 0
    for i := 1; i < len(result); i++ {
        result[i] = xs[i-1] * i
    }
    return result
}



