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
	for i := len(str) - 1; i >= 0; i-- {
		if IsPalindrome(str[i+1:]) {
			return str + Reverse(str[:i+1])
		}
	}
	return str + Reverse(str)
}

// Reverse the given string.
func Reverse(str string) string {
	runes := []rune(str)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
```