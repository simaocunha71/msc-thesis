    result := make([]int, 0)

    for _, value := range values {
        if val, ok := value.(int); ok {
            result = append(result, val)
        }
    }

    return result
}



