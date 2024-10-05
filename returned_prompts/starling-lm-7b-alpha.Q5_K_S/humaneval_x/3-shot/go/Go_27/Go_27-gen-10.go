    result := make([]rune, len(str))
    for i, c := range str {
        if c >= 'a' && c <= 'z' {
            result[i] = c - 32
        } else if c >= 'A' && c <= 'Z' {
            result[i] = c + 32
        } else {
            result[i] = c
        }
    }
    return string(result)
}



