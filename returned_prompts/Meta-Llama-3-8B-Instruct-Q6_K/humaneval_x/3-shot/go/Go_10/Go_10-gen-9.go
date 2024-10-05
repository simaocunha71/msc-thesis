    runes := []rune(str)
    for i := len(runes) - 1; i > 0; i-- {
        if !IsPalindrome(string(runes[:i+1])) {
            break
        }
    }
    return str + reverse(string(runes[:i])) + str[i:]
}

func reverse(str string) string {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}
func IsPalindrome(str string) bool {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return str == string(result)
}