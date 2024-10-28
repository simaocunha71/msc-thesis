    result := make([]string, 0)

    for _, v := range strings {
        if strings.HasPrefix(v, prefix) {
            result = append(result, v)
        }
    }
    return result
}



