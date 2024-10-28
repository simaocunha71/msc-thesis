    result := make([]int, 0)
    for _, v := range values {
        switch v := v.(type) {
        case int:
            result = append(result, v)
        }
    }
    return result
}



