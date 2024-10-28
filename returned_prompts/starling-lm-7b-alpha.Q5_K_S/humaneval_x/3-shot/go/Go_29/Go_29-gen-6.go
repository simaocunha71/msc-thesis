    result := make([]string, 0)
    for _, s := range strings {
        if stringUtils.StartsWith(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}



