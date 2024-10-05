    result := make([]rune, len(a))
    for i, v := range a {
        result[i] = v ^ b[i]
    }
    return string(result)
}




