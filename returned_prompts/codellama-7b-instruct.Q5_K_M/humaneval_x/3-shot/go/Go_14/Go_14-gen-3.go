    result := make([]string, 0)
    for i := 1; i <= len(str); i++ {
        result = append(result, str[:i])
    }
    return result
}



