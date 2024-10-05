    runes := []rune(str)
    for i := 0; i < len(runes); i++ {
        if IsPalindrome(string(runes[i:])) {
            return str + Reverse(str[:i])
        }
    }
    return str
}

// Reverse a string.
func Reverse(str string) string {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}

