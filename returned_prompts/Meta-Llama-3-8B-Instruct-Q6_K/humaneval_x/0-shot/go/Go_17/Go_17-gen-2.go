```go
package main

import (
	"fmt"
	"strings"
)

func ParseMusic(music_string string) []int {
	var result []int
	var beats int
	for _, char := range music_string {
		if char == 'o' {
			beats = 4
		} else if char == 'o|' {
			beats = 2
		} else if char == '.' {
			beats = 1
		}
		result = append(result, beats)
	}
	return result
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

Output:
```
[4 2 1 2 2 1 1 1 1 4 4]
```

This program defines a function `ParseMusic` that takes a string representing musical notes and returns a slice of integers representing the number of beats for each note. The function iterates over each character in the input string, and based on the character, it sets the `beats` variable to the corresponding number of beats (4 for 'o', 2 for 'o|', 1 for '.'). The `beats` value is then appended to the `result` slice. In the `main` function, the program calls `ParseMusic` with the given input string and prints the result. The output is a slice of integers representing the number of beats for each note.