    result := make([]byte, 0)
    for _, c := range message {
        if c >= 'a' && c <= 'z' {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                result = append(result, byte('z' - 'a' + c + 2))
            } else {
                result = append(result, byte(c + 1))
            }
        } else if c >= 'A' && c <= 'Z' {
            if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
                result = append(result, byte('Z' - 'A' + c + 2))
            } else {
                result = append(result, byte(c + 1))
            }
        } else {
            result = append(result, byte(c))
        }
    }
    return strings.NewString(result)
} 



