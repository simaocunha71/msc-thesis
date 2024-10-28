You can use regular expressions in Go to remove vowels from a string. Here's how you can implement the RemoveVowels function:

```go
package main

import (
	"fmt"
	"regexp"
)

func RemoveVowels(text string) string {
	vowelRegex := regexp.MustCompile("[aeiouAEIOU]")
	return vowelRegex.ReplaceAllString(text, "")
}

func main() {
	fmt.Println(RemoveVowels(""))          // Output: ""
	fmt.Println(RemoveVowels("abcdef\nghijklm")) // Output: "bcdf\nghjklm"
	fmt.Println(RemoveVowels("abcdef"))      // Output: "bcdf"
	fmt.Println(RemoveVowels("aaaaa"))       // Output: ""
	fmt.Println(RemoveVowels("aaBAA"))       // Output: "B"
	fmt.Println(RemoveVowels("zbcd"))        // Output: "zbcd"
}
```

This function uses the `regexp` package to create a regular expression that matches any vowel (both lowercase and uppercase). It then uses the `ReplaceAllString` method to remove all matching characters from the input string.

The `main` function demonstrates how to use the `RemoveVowels` function with various inputs, and prints the results.