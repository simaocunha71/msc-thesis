    // find the longest postfix that is palindrome
    for i := 0; i < len(str); i++ {
        if !IsPalindrome(str[i:]){
            break
        }
    }
    // reverse the prefix and add to the end
    return str + reverse(str[:i])
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
    return s == string(result)
}