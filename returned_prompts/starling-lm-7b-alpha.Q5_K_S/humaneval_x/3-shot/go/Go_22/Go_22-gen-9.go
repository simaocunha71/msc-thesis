    result := make([]int, 0)
    for _, v := range values {
        if i, ok := v.(int); ok {
            result = append(result, i)
        }
    }
    return result
}



