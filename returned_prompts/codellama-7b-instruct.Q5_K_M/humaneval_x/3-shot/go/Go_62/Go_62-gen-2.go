    result := make([]int, len(xs))
    for i := 1; i < len(xs); i++ {
        result[i] = xs[i] * (i + 1)
    }
    return result
}



