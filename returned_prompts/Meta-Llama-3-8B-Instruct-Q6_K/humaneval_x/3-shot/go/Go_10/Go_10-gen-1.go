    s := strings.ToLower(str)
    for i := len(s); i > 0; i-- {
        if IsPalindrome(s[:i]) {
            return str + reverse(s[i:])
        }
    }
    return str
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