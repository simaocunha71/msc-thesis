    result := make([]rune, 0)
    for _, c := range strings.ToUpper(message) {
        if c >= 'A' && c <= 'Z' {
            if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
                result = append(result, rune((c - 'A' + 2) % 26 + 'A'))
            } else {
                result = append(result, c)
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}