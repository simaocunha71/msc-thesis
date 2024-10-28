    result := make([]rune, 0, len(s))
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result = append(result, rune(c - 'a' + 'A'))
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, rune(c - 'A' + 'a'))
        } else {
            result = append(result, c)
        }
    }
    if len(result) == 0 {
        return reverse(s)
    }
    return string(result)
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}