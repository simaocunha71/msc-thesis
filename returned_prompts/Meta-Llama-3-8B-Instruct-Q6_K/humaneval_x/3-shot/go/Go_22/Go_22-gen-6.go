    result := make([]int, 0)
    for _, value := range values {
        v, ok := value.(int)
        if ok {
            result = append(result, v)
        }
    }
    return result
}