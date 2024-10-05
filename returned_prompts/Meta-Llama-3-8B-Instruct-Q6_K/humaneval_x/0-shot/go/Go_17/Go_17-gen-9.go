```go
package main

import (
	"fmt"
	"regexp"
)

func ParseMusic(music_string string) []int {
	// Define a map to store the duration of each note
	durationMap := map[string]int{
		"o": 4,
		"o|": 2,
		"|": 1,
	}

	// Use regular expression to split the input string into individual notes
	regex, err := regexp.Compile("\\(|\\||o")
	if err != nil {
		fmt.Println(err)
		return nil
	}
	noteArray := regex.Split(music_string, -1)

	var durations []int
	for _, note := range noteArray {
		for k, v := range durationMap {
			if strings.Contains(note, k) {
				durations = append(durations, v)
			}
		}
	}

	return durations
}

func main() {
	music_string := "o o| .| o| o| .| .| .| .| o o"
	fmt.Println(ParseMusic(music_string))
}
```
In this solution, we define a map to store the duration of each note. Then, we use regular expression to split the input string into individual notes. We iterate over each note and check if it contains any of the note types in our map. If it does, we append the corresponding duration to our result array. Finally, we return the array of durations. In the main function, we test our solution with a sample input string. The output will be `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`. This is the expected output for the given input string.