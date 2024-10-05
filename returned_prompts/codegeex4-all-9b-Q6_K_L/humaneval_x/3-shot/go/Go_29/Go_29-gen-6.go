    result := make([]string,0)
    for _, s := range strings {
        if s[:len(prefix)] == prefix {
            result = append(result, s)
        }
    }
    return result
}



