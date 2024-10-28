    result  := make([]int, 0, len(xs)-1)
    for i, v := range xs[1:] {
        result = append(result, (i+1)*v)
    }
    return result
}



