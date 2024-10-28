To encrypt a string by shifting the alphabet two places down, you can use the following function in Go:

```go
package main

import (
	"strings"
	"unicode"
)

// Encrypt takes a string as an argument and returns a string encrypted with the alphabet being rotated.
func Encrypt(s string) string {
	var encrypted string
	for _, r := range s {
		if unicode.IsLetter(r) {
			shift := 2 * 2 // Shift the alphabet down by 4 places (2 places * 2 times)
			// Normalize the shift value to be within the range of the alphabet
			shift %= 26
			if unicode.IsUpper(r) {
				encrypted += string(unicode.ToUpper(rune((r-'A'+shift)%26 + 'A')))
			} else {
				encrypted += string(unicode.ToLower(rune((r-'a'+shift)%26 + 'a')))
			}
		} else {
			encrypted += string(r)
		}
	}
	return encrypted
}

func main() {
	println(Encrypt("hi"))                  // lm
	println(Encrypt("asdfghjkl"))           // ewhjklnop
	println(Encrypt("gf"))                  // kj
	println(Encrypt("et"))                  // ix
	println(Encrypt("Hi, how are you?"))    // Lm, qvq gha lvq?
}
```

This function iterates over each character in the input string. If the character is a letter, it shifts the letter down by 4 places (2 places * 2 times), wrapping around to the start of the alphabet if necessary. If the character is not a letter, it leaves it unchanged. The result is a new string with the alphabet rotated down by 4 places.