    result := make([]int, len(xs)-1)
    for i := 1; i < len(result); i++ {
        result[i-1] = xs[i] * i
    }
    return result
}



