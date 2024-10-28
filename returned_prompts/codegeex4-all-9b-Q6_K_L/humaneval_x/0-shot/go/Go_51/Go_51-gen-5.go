```go
package main

import (
	"regexp"
	"strings"
)

func RemoveVowels(text string) string {
	vowels := regexp.MustCompile("[aeiouAEIOU]")
	return vowels.ReplaceAllString(text, "")
}

func main() {
	println(RemoveVowels(""))
	println(RemoveVowels("abcdef\nghijklm"))
	println(RemoveVowels("abcdef"))
	println(RemoveVowels("aaaaa"))
	println(RemoveVowels("aaBAA"))
	println(RemoveVowels("zbcd"))
}
```
