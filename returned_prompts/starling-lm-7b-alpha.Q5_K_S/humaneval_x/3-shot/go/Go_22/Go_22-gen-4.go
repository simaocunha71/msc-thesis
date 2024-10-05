    result := make([]int, 0)
    for _, value := range values {
        switch v := value.(type) {
        case int:
            result = append(result, v)
        }
    }
    return result
}



