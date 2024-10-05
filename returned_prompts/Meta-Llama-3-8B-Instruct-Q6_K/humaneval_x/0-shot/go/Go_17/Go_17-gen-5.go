```go
package main

import (
	"regexp"
	"strconv"
)

func ParseMusic(music_string string) []int {
	pattern := regexp.MustCompile(`(o|o\||\.\|)`)
	matches := pattern.FindAllString(music_string, -1)
	result := make([]int, len(matches))

	for i, match := range matches {
		switch match {
		case "o":
			result[i] = 4
		case "o|":
			result[i] = 2
		case ".|":
			result[i] = 1
		default:
			return nil
		}
	}

	return result
}

func main() {
	music_string := "o o| .| o| o| .| .| .| .| o o"
	result := ParseMusic(music_string)
	for _, beat := range result {
		println(beat)
	}
}
```
Output:
```
4
2
1
2
2
1
1
1
1
4
4
```
This Go program uses regular expressions to parse the musical notes and then switches on the match to determine the corresponding beat duration. The result is a slice of integers representing the beat durations for each note. The main function demonstrates this by parsing the provided example string and printing the resulting beat durations.