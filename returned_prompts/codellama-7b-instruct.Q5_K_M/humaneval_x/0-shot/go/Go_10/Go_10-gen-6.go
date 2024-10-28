import (
    "strings"
)

// Test if given string is a palindrome.
func IsPalindrome(str string) bool {
    return strings.Index(str, str) == 0
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
    i := len(str) - 1
    for ; i >= 0; i-- {
        if IsPalindrome(str[i:]) {
            break
        }
    }
    return str[i:] + strings.Trim(str[:i], str[i:])
}
