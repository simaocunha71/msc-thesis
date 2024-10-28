    result := make([]string, 0)
    for i := 0; i <= len(str); i++ {
        result = append(result, str[:i+1])
    }
    return result
}  // because the problem asks for prefixes, so the last element should be the full string itself.  // Because of the loop, the last element will be the full string itself.