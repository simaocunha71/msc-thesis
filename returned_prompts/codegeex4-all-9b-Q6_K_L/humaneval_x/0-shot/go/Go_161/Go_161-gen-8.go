You can solve this problem by iterating through the string and checking each character. If the character is a letter, you can use the `unicode` package to check its case and reverse it accordingly. If the character is not a letter, you can keep it as it is. If the string contains no letters, you can use the `strings` package to reverse the entire string. Here is the solution in Go:

```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func Solve(s string) string {
	hasLetter := false
	result := ""

	for _, r := range s {
		if unicode.IsLetter(r) {
			hasLetter = true
			if unicode.IsLower(r) {
				result += string(unicode.ToUpper(r))
			} else {
				result += string(unicode.ToLower(r))
			}
		} else {
			result += string(r)
		}
	}

	if !hasLetter {
		return strings.Reverse(result)
	}

	return result
}

func main() {
	fmt.Println(Solve("1234")) // "4321"
	fmt.Println(Solve("ab"))   // "AB"
	fmt.Println(Solve("#a@C")) // "#A@c"
}
```

This solution uses the `unicode` package to check if a character is a letter and its case, and the `strings` package to reverse the entire string if it contains no letters. The `Solve` function iterates through the string and builds the result string based on the conditions mentioned.