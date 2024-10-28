    result := make([]rune, 0)
    for _, string := range strings {
        result = append(result, ...string)
    }
    return string(result)
}



