    result := make([]rune, 0)

    for _, c := range strings.ToUpper(message) {
        if c >= 'A' && c <= 'Z' {
            if c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
                result = append(result, rune('K' + (c - 'A'))[0])
            }else {
                result = append(result, rune(c))
            }
        }else if c >= 'a' && c <= 'z' {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                result = append(result, rune('k' + (c - 'a'))[0])
            }else {
                result = append(result, rune(c))
            }
        }else {
            result = append(result, c)
        }
    }
    return string(result)
}