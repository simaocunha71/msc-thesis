    result := make([]int, 0)

    for _, v := range values {
        if val, ok := v.(int); ok {
            result = append(result, val)
        }
    }

    return result
}



