    result := make([]byte, 0)
    for _, c := range message {
        if 'a' <= c && c <= 'z' {
            result = append(result, byte('a' + (c - 'a' + 2) % 26))
        } else if 'A' <= c && c <= 'Z' {
            result = append(result, byte('A' + (c - 'A' + 2) % 26))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}