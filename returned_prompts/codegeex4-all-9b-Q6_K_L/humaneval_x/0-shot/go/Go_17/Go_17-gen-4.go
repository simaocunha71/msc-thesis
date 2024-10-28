Here is a Go solution that uses a regular expression to match the note patterns and then calculates the duration of each note:

```go
package main

import (
	"fmt"
	"regexp"
)

func ParseMusic(music_string string) []int {
	var durations []int
	r := regexp.MustCompile(`o|\.\|`)

	for _, match := range r.FindAllStringSubmatch(music_string, -1) {
		switch match[0] {
		case "o":
			durations = append(durations, 4)
		case ".|":
			durations = append(durations, 1)
		}
	}

	return durations
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

This solution works by creating a regular expression that matches either "o" or ".|" and then using the `FindAllStringSubmatch` function to find all occurrences of these patterns in the input string. For each match, it then checks if the match is "o" or ".|" and appends the corresponding duration to the `durations` slice.

Note: This solution assumes that the input string is always valid and contains only the characters "o", "|", and ".". If the input string can contain other characters, you may need to add additional error checking to handle these cases.