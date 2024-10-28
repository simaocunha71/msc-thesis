    result := make([]byte, 0, len(str))
    for _, c := range str {
        if c >= 'a' && c <= 'z' {
            result = append(result, byte(c - 'a' + 'A'))
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, byte(c - 'A' + 'a'))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}