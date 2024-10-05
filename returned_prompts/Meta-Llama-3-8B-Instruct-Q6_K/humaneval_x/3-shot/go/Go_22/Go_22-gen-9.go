    var result []int
    for _, value := range values {
        if v, ok := value.(int); ok {
            result = append(result, v)
        }
    }
    return result
}



