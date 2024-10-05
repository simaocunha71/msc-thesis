    result := make([]byte, 0)
    for _, c := range s {
        if 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' {
            if c >= 'a' && c <= 'z' {
                result = append(result, byte(c - 'a' + 'A'))
            } else {
                result = append(result, byte(c))
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}  // Note: This solution assumes that the input string will not contain non-ASCII characters. If you need to support non-ASCII characters, you would need to use a different approach, such as using Unicode properties or a library like `strings`.