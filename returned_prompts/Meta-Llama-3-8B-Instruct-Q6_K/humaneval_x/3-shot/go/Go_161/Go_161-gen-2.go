    result := make([]byte, 0)
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result = append(result, byte(c - 'a' + 'A'))
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, byte(c + 'a' - 'A'))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}