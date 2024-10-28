    result := make([]int, 0)
    for i := 1; i < len(xs); i++ {
        result = append(result, xs[i] * i)
    }
    return result
}



