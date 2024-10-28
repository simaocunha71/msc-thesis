    result := make([]int, 0)

    for _, v := range values {
        if _, ok := v.(int); ok {
            result = append(result, v.(int))
        }
    }
    return result
}



