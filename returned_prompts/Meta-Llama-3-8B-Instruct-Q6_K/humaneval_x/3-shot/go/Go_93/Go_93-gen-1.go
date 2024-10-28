    encoded := make([]byte, 0)
    for _, c := range strings.ToUpper(message) {
        if c >= 'A' && c <= 'Z' {
            encoded = append(encoded, byte(c+1))
        } else if c >= 'a' && c <= 'z' {
            encoded = append(encoded, byte(c+1))
        } else {
            encoded = append(encoded, c)
        }
    }
    return string(encoded)
}