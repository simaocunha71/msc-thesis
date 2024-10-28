    if len(str) == 0 {
        return ""
    }
    for i := len(str) - 1; i > 0; i-- {
        if IsPalindrome(str[:i+1]) {
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

func IsPalindrome(s string) bool {
    runes := []rune(s)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result) == s
}