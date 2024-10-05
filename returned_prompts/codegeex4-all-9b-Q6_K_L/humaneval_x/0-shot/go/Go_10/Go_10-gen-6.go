func MakePalindrome(str string) string {
    for i := len(str); i > 0; i-- {
        if IsPalindrome(str[:i]) {
            return str + Reverse(str[:i])
        }
    }
    return str
}

// Reverse a string.
func Reverse(s string) string {
    runes := []rune(s)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}

// Test if given string is a palindrome.
func IsPalindrome(str string) bool {
    runes := []rune(str)
    for i := 0; i < len(runes)/2; i++ {
        if runes[i] != runes[len(runes)-i-1] {
            return false
        }
    }
    return true
}