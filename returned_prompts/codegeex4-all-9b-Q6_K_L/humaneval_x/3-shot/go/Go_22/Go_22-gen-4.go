    result := make([]int, 0)
    for _, val := range values {
        if _, ok := val.(int); ok {
            result = append(result, val.(int))
        }
    }
    return result
}



