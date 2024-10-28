    result := make([]rune, 0, len(s))
    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            result = append(result, byte(c-32))
        } else if 'A' <= c && c <= 'Z' {
            result = append(result, byte(c+32))
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