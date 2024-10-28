    result := make([]rune, len(s))

    for i, c := range s {
        if c >= 'a' && c <= 'z' {
            result[i] = c - 'a' + 'A'
        } else if c >= 'A' && c <= 'Z' {
            result[i] = c - 'A' + 'a'
        } else {
            result[i] = c
        }
    }

    return string(result)
}

