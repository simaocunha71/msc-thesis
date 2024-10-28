    result := make([]int, 0)
    for _, value := range values {
        if value, ok := value.(int); ok {
            result = append(result, value)
        }
    }
    return result
}

