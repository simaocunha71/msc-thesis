    result := make([]rune, 0)
    for _, s := range strings {
        result = append(result, ...s)
    }
    return string(result)
}



