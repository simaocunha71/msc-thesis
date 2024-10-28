```go
package main

import (
	"fmt"
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
func MakePalindrome(str string) string {
	if IsPalindrome(str) {
		return str
	}
	for i := len(str); i > 0; i-- {
		if IsPalindrome(str[i:]) {
			return str + Reverse(str[:i])
		}
	}
	return ""
}

// Reverse a string
func Reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	fmt.Println(MakePalindrome("cat"))
	fmt.Println(MakePalindrome("cata"))
	fmt.Println(MakePalindrome(""))
}
```
This Go code defines two functions `IsPalindrome` and `MakePalindrome`. The `IsPalindrome` function checks if a given string is a palindrome. The `MakePalindrome` function finds the shortest palindrome that begins with a given string. It does this by finding the longest postfix of the given string that is a palindrome and appending the reverse of the prefix that comes before the palindromic suffix to the end of the string. The `Reverse` function is used to reverse a string. The `main` function is used to test the `MakePalindrome` function with some example strings.