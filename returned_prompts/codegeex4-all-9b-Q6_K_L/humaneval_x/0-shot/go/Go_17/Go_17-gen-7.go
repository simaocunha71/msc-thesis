Here is a solution that uses a regular expression to match the music notes and then converts them to their corresponding beat lengths:

```go
package main

import (
	"fmt"
	"regexp"
)

func ParseMusic(music_string string) []int {
	var beats []int
	// Regular expression to match the music notes
	re := regexp.MustCompile(`o|o\||\.\|`)
	// Find all matches in the input string
	matches := re.FindAllString(music_string, -1)
	// Convert each match to its corresponding beat length
	for _, match := range matches {
		switch match {
		case "o":
			beats = append(beats, 4)
		case "o|":
			beats = append(beats, 2)
		case ".|":
			beats = append(beats, 1)
		}
	}
	return beats
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

This solution first defines a regular expression that matches the three music notes. It then uses the `FindAllString` function to find all matches in the input string. For each match, it checks which note it is and appends the corresponding beat length to the `beats` slice. Finally, it returns the `beats` slice.