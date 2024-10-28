    result := make([]string, 0)

    for _, string := range strings {
        if strings.HasPrefix(string, prefix) {
            result = append(result, string)
        }
    }
    return result
}



