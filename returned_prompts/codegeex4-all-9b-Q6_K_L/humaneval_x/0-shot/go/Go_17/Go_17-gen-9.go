You can use the `strings.FieldsFunc` function to split the string into an array of tokens. Then, you can iterate over the tokens and check their length to determine the number of beats. Here's a possible implementation:

```go
package main

import (
	"fmt"
	"strings"
)

func ParseMusic(music_string string) []int {
	tokens := strings.FieldsFunc(music_string, func(r rune) bool {
		return r == ' '
	})

	result := make([]int, len(tokens))
	for i, token := range tokens {
		switch len(token) {
		case 1:
			result[i] = 4
		case 2:
			if token[1] == '|' {
				result[i] = 2
			} else {
				result[i] = 1
			}
		}
	}

	return result
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

In this code, the `FieldsFunc` function splits the input string into an array of tokens using a custom function that checks for spaces. Then, we iterate over the tokens and check their length to determine the number of beats. The result is stored in a slice of integers and returned.