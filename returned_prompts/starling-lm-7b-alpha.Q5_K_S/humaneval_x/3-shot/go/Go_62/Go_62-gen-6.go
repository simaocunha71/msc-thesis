    result := make([]int, 0)
    if len(xs) > 0 {
        result = append(result, xs[0])
    }
    for i := 1; i < len(xs); i++ {
        result = append(result, result[len(result)-1]+i*xs[i])
    }
    return result
}



