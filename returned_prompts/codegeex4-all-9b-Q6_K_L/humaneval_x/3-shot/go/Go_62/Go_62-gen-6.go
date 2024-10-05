    var result []int
    if len(xs) == 0 {
        return result
    }
    for i := 1; i < len(xs); i++ {
        result = append(result, xs[i]*i)
    }
    return result
}

