You can use the strings package in Go to check if a character is a letter or not. Here's the function Solve that implements the logic you described:

```go
package main

import (
	"strings"
)

func Solve(s string) string {
	// Check if the string contains any letters
	if !strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
		// Reverse the string if it contains no letters
		return Reverse(s)
	}

	// Reverse the case of each letter in the string
	result := ""
	for _, c := range s {
		if strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", c) {
			// Reverse the case of the letter
			if 'a' <= c && c <= 'z' {
				result += string(c - 'a' + 'A')
			} else {
				result += string(c - 'A' + 'a')
			}
		} else {
			// Keep non-letter characters as they are
			result += string(c)
		}
	}

	return result
}

// Reverse reverses a string
func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	// Test the Solve function
	println(Solve("1234"))        // Output: "4321"
	println(Solve("ab"))          // Output: "AB"
	println(Solve("#a@C"))        // Output: "#A@c"
	println(Solve("Hello, World")) // Output: "DLROw ,olleH"
}
```

In this solution, we first check if the string contains any letters using the strings.ContainsAny function. If it doesn't, we reverse the string using the Reverse function.

If the string contains letters, we iterate through each character and check if it is a letter using the strings.ContainsRune function. If it is a letter, we reverse its case by converting it to uppercase or lowercase using the 'a' and 'A' constants. If it is not a letter, we keep it as it is.

Finally, we return the resulting string.