    result := make([]rune, 0)
    for i := 0; i < len(s); i += 3 {
        if i+3 <= len(s) {
            runes := []rune(s[i:i+3])
            result = append(result, runes[0])
        } else {
            runes := []rune(s[i:])
            result = append(result, runes...)
        }
    }
    return string(result)
}