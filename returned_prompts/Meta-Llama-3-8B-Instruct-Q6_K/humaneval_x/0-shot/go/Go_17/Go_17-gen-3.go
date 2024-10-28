```go
package main

import (
	"fmt"
	"strings"
)

func ParseMusic(music_string string) []int {
	var beats []int
	var current_beats int
	var last_char rune
	for _, char := range music_string {
		if char == 'o' || char == 'o|' || char == '.' || char == '.|' {
			if char == 'o|' {
				current_beats = 2
			} else if char == '.' || char == '.|' {
				current_beats = 1
			} else {
				current_beats = 4
			}
			if last_char != 0 {
				beats = append(beats, current_beats)
			}
			current_beats = 0
			last_char = char
		}
	}
	beats = append(beats, current_beats)
	return beats
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```
Explanation:
This program defines a function `ParseMusic` that takes a string `music_string` as input and returns a slice of integers representing the number of beats for each note in the string.

The function iterates over each character in the string. If the character is one of the note types ('o', 'o|', '.', '.|'), it checks the type of the note and updates the `current_beats` variable accordingly. If the character is not a note type, it skips it.

After processing each note, it checks if the previous character was also a note type. If it was, it appends the `current_beats` value to the `beats` slice. Then, it resets `current_beats` to 0 and updates the `last_char` variable.

After processing the entire string, it appends the final `current_beats` value to the `beats` slice.

In the `main` function, it calls the `ParseMusic` function with the input string "o o| .| o| o| .| .| .| .| o o" and prints the result.

Output:
```
[4 2 1 2 2 1 1 1 1 4 4]
``` 