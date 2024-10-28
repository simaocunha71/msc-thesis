```
return !strings.ContainsAny(text, " ") && strings.EqualFold(text, reverseString(text))
```
Explanation:

1. `strings.ContainsAny(text, " ")`: This function checks if the given string `text` contains any whitespace characters. If it does, it means the string is not a palindrome, so we return `false`.
2. `strings.EqualFold(text, reverseString(text))`: This function checks if the given string `text` is equal to its reverse. If it is, it means the string is a palindrome. The `EqualFold` function is used to ignore the case of the letters. The `reverseString` function is not a built-in function in Go, so you need to define it yourself.

Here's the complete code:
```go
package main

import (
	"fmt"
	"strings"
)

func reverseString(text string) string {
	runes := []rune(text)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func IsPalindrome(text string) bool {
	return !strings.ContainsAny(text, " ") && strings.EqualFold(text, reverseString(text))
}

func main() {
	fmt.Println(IsPalindrome(""))        // true
	fmt.Println(IsPalindrome("aba"))     // true
	fmt.Println(IsPalindrome("aaaaa"))   // true
	fmt.Println(IsPalindrome("zbcd"))    // false
}
```
This code defines a function `IsPalindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome or not. The function first checks if the string contains any whitespace characters, and if it does, it returns `false`. If it doesn't, it checks if the string is equal to its reverse, ignoring case. If it is, it returns `true`. The `main` function demonstrates the usage of the `IsPalindrome` function with different inputs.