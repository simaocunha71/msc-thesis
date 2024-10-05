    result := make([]int, 0)
    for _, value := range values {
        if _, ok := value.(int); ok {
            result = append(result, value.(int))
        }
    }
    return result
}



