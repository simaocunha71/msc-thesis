    if strings.ToLower(str) == strings.ToLower(reverse(str)) {
        return str
    }
    for i := len(str) - 1; i > 0; i-- {
        if strings.ToLower(str[:i]) == strings.ToLower(reverse(str[i:])) {
            return str + reverse(str[:i])
        }
    }
    return str + reverse(str)
}

func reverse(s string) string {
    runes := []rune(s)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}