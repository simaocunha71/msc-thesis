    result := make([]string, 0)
    for _, s := range strings {
        if len(s) > 0 && s[0] == rune(prefix[0]) {
            result = append(result, s)
        }
    }
    return result
}



