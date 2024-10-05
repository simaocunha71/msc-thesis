    result := make([]int, len(xs))
    if len(xs) == 0 {
        return result
    }
    result[0] = 0
    for i := 1; i < len(xs); i++ {
        result[i] = xs[i-1] * i
    }
    return result
}



