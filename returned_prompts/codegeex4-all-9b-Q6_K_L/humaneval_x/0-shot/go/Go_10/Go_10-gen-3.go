```go
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
    for i := len(str); i > 0; i-- {
        if IsPalindrome(str[i:]) {
            return str + Reverse(str[:i])
        }
    }
    return str
}

// Reverse given string.
func Reverse(str string) string {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}
```
This code defines two functions, `IsPalindrome` and `MakePalindrome`, and a helper function `Reverse`. 

The `IsPalindrome` function checks if a given string is a palindrome by comparing the string with its reverse.

The `MakePalindrome` function finds the shortest palindrome that begins with a supplied string. It uses a loop to find the longest postfix of the supplied string that is a palindrome, and then appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string.

The `Reverse` function reverses a given string by converting it to a slice of runes, reversing the slice, and then converting it back to a string.