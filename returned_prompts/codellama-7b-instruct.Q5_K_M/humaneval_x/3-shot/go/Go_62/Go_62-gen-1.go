    result := make([]int, len(xs)-1)
    for i := 0; i < len(xs)-1; i++ {
        result[i] = xs[i+1] * (i+1)
    }

    return result
}



