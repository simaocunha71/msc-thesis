    var result []int
    for _, value := range values {
        if i, ok := value.(int); ok {
            result = append(result, i)
        }
    }
    return result
}