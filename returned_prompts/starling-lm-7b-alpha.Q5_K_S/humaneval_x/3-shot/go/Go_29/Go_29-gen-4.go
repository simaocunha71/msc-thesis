    result := make([]string, 0)
    for _, string_ := range strings {
        if string_.StartsWith(prefix) {
            result = append(result, string_)
        }
    }
    return result
}



