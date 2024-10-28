    result := make([]byte, 0)
    for _, c := range strings.ToUpper(message) {
        if c >= 'A' && c <= 'Z' {
            if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
                result = append(result, byte(c + 2))
            } else {
                result = append(result, byte(c))
            }
        } else if c >= 'a' && c <= 'z' {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                result = append(result, byte(c + 2))
            } else {
                result = append(result, byte(c))
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}