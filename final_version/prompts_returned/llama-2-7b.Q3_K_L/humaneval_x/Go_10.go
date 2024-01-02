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
    // Find the longest postfix of supplied string that is a palindrome.
    var maxlen = 1
    for i := len(str) - 2; i >= 0; i-- {
        if (IsPalindrome(string(str[i:]))) && (maxlen < len(string(str[i:]))) {
            maxlen = len(string(str[i:]))
        }
    }
    // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    reverseStr := strings.ReverseString(strings.ToLower(str[:maxlen])) + "c"
    return str + strings.Join(strings.Split(reverseStr, "c"), "")
}
