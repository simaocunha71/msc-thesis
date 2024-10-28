    result := make([]string, 0)
    for _, s := range strings {
        if string(s[0]) == prefix[0] {
            result = append(result, s)
        }
    }
    return result
}



