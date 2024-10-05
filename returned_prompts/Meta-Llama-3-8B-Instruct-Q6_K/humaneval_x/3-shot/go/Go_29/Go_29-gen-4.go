    result := make([]string, 0)
    for _, str := range strings {
        if len(str) >= len(prefix) && str[:len(prefix)] == prefix {
            result = append(result, str)
        }
    }
    return result
}