
	beat_values := make([]int, 0)
	notes := strings.Split(music_string, " ")

	for _, note := range notes {

		switch note {
		case "o":
			beat_values = append(beat_values, 4)
		case "o|":
			beat_values = append(beat_values, 2)
		case ".|":
			beat_values = append(beat_values, 1)
		default:
			continue
		}
	}

	return beat_values
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o")) // [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
}
```

## 4. Palindrome

A palindrome is a word, number, phrase or other sequences of characters that reads the same backward as forward.

Write a function that takes a string input, and checks if it is a palindrome. Return `True` if it is, and `False` if it isn't. Ignore spaces, punctuation, and case sensitivity.

```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

// Input to this function is a string which may or may not be a palindrome.
// Your task is to check if the string is a palindrome or not.
// You should ignore spaces, punctuation and case sensitivity.
// 
// >>> IsPalindrome('Was it a car or a cat I saw')
// True
// 
// >>> IsPalindrome('Hello World')
// False

func IsPalindrome(str string) bool {
	str = strings.ToLower(str)
	str = strings.ReplaceAll(str, " ", "")
	str = strings.Map(func(r rune) rune {
		if unicode.IsLetter(r) || unicode.IsDigit(r) {
			return r
		}
		return -1
	}, str