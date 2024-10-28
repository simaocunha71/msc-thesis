    var result []int
    for _, v := range values {
        if t, ok := v.(int); ok {
            result = append(result, t)
        }
    }
    return result
}