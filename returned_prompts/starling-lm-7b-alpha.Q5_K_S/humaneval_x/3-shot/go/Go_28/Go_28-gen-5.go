    result := make([]rune, 0)
    for _, s := range strings {
        for _, r := range s {
            result = append(result, r)
        }
    }
    return string(result)
}



