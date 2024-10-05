    result := make([]rune, 0)
    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            result = append(result, c - 32)
        } else if 'A' <= c && c <= 'Z' {
            result = append(result, c + 32)
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}



