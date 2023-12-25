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
    str = strings.TrimSpace(str)
    if IsPalindrome(str) && len(str) == 1 {
        return str + string(RuneError())
    }
    var max = -1
    for i := range Strings() {
        pfx, err := MakePrefix(strings.TrimSpace(str[:i]))
        if IsPalindrome(strings.Join([]rune{pfx}, "")) && len(str) > 1+i+1 {
            max = i + 1
            str += strings.Join([]rune{strings.Reverse(string(RuneError()))[max:]}, "") + string(RuneError())
        }
    }
    return str
}