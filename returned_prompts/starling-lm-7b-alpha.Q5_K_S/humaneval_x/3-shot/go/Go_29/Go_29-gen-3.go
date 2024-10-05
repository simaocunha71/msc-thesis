    result := make([]string, 0)
    for _, s := range strings {
        if len(s) > 0 && s[0:len(prefix)] == prefix {
            result = append(result, s)
        }
    }
    return result
}



