    result := make([]int, 0)
    for _, v := range values {
        i, ok := v.(int)
        if ok {
            result = append(result, i)
        }
    }
    return result
}



