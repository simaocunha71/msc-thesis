```go
package main

import (
	"regexp"
)

// RemoveVowels is a function that takes string and returns string without vowels.
func RemoveVowels(text string) string {
	vowelRegex := regexp.MustCompile("[aeiouAEIOU]")
	return vowelRegex.ReplaceAllString(text, "")
}
```