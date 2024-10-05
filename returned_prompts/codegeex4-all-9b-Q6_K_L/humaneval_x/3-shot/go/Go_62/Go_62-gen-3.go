    result := make([]int, 0)
    for i := 1; i < len(xs); i++ {
        result = append(result, i*xs[i])
    }
    return result
}



