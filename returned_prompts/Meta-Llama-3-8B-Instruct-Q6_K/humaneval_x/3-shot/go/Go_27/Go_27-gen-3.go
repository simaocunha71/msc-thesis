    result := make([]byte, 0)
    for _, c := range str {
        if c >= 'a' && c <= 'z' {
            result = append(result, byte(c - 32))
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, byte(c + 32))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}