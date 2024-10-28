    var result []int
    for _, v := range values {
        if val, ok := v.(int); ok {
            result = append(result, val)
        }
    }
    return result
}