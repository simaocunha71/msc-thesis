    result := make([]rune, 0)
    for _, s := range strings {
        result = append(result, []rune(s)...)
    }
    return string(result)
}



