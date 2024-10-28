    var result []int
    for _, value := range values {
        if val, ok := value.(int); ok {
            result = append(result, val)
        }
    }
    return result
}



