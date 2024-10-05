    result := make([]int, 0)

    for _, value := range values {
        if v, ok := value.(int); ok {
            result = append(result, v)
        }
    }

    return result
}



