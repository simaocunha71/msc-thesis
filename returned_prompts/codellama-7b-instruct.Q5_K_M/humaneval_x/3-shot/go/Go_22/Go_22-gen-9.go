    result := make([]int, 0)
    for _, value := range values {
        switch value.(type) {
        case int:
            result = append(result, value.(int))
        }
    }
    return result
}



