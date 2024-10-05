    result  := make([]string, 0)
    for _, str := range strings {
        if strings.HasPrefix(str, prefix) {
            result = append(result, str)
        }
    }
    return result
}



