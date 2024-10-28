    result := make([]int, len(xs)-1)
    for i := 1; i < len(xs); i++ {
        result[i-1] = i * xs[i]
    }
    return result
}



