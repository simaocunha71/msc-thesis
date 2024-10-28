    result := make([]int, 0)
    for i, x := range xs {
        if i == 0 {
            continue
        }
        result = append(result, x*i)
    }
    return result
}



