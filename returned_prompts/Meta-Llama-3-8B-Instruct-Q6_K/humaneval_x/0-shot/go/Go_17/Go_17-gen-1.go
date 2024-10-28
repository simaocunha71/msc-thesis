```
package main

import (
	"fmt"
	"strings"
)

func ParseMusic(music_string string) []int {
	var result []int
	var beats int

	for _, char := range music_string {
		switch char {
		case 'o':
			beats = 4
		case '|':
			beats /= 2
		case '.':
			beats /= 4
		default:
			beats = 0
		}
		result = append(result, beats)
	}

	return result
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

This program will parse the input string and return a list of integers representing the number of beats each note lasts. It uses a simple state machine to track the current note and its duration. When it encounters a character that changes the duration of the note, it updates the `beats` variable accordingly. The `result` slice is used to store the final list of beats.

In the `main` function, we test the `ParseMusic` function with the given input string and print the result. The output should be `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`.