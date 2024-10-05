import (
    "strings"
)

// Test if given string is a palindrome.
func IsPalindrome(str string) bool {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return str == string(result)
}
// Find the shortest palindrome that begins with a supplied string.
// Algorithm idea is simple:
// - Find the longest postfix of supplied string that is a palindrome.
// - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
// >>> MakePalindrome('')
// ''
// >>> MakePalindrome('cat')
// 'catac'
// >>> MakePalindrome('cata')
// 'catac'
func MakePalindrome(str string) string {
    if IsPalindrome(str) {
        return str
    }
    var suffix string
    var prefix string
    for i := len(str) - 1; i >= 0; i-- {
        if IsPalindrome(str[:i+1]) {
            suffix = str[i+1:]
            prefix = str[:i]
            break
        }
    }
    if suffix == "" {
        return ""
    }
    return prefix + strings.Reverse(suffix)
}

