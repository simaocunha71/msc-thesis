    result := make([]rune, len(message))
    for i, c := range message {
        if c >= 'a' && c <= 'z' {
            result[i] = rune(int(c) - 22)
        } else if c >= 'A' && c <= 'Z' {
            result[i] = rune(int(c) + 22)
        } else {
            result[i] = c
        }
    }
    return string(result)
}



