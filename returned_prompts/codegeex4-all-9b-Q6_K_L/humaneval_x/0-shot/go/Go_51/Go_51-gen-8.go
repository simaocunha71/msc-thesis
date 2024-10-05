```go
package main

import (
	"fmt"
	"regexp"
)

func RemoveVowels(text string) string {
	re := regexp.MustCompile("[aeiouAEIOU]")
	return re.ReplaceAllString(text, "")
}

func main() {
	fmt.Println(RemoveVowels(""))
	fmt.Println(RemoveVowels("abcdef\nghijklm"))
	fmt.Println(RemoveVowels("abcdef"))
	fmt.Println(RemoveVowels("aaaaa"))
	fmt.Println(RemoveVowels("aaBAA"))
	fmt.Println(RemoveVowels("zbcd"))
}
```
This code defines a function `RemoveVowels` that takes a string and returns a new string with all vowels removed. It uses a regular expression to match and replace all vowel characters with an empty string. The function is then tested with various input strings to ensure it behaves as expected.