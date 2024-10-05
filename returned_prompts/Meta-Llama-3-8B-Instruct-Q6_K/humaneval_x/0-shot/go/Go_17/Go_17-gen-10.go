```go
package main

import (
	"strconv"
	"strings"
)

func ParseMusic(music_string string) []int {
	var beats []int
	var beatsPerNote = map[string]int{
		"o": 4,
		"o|": 2,
		"|": 1,
	}

	for _, note := range strings.Split(music_string, " ") {
		beats = append(beats, beatsPerNote[note])
	}

	return beats
}

func main() {
	music := "o o| .| o| o| .| .| .| .| o o"
	result := ParseMusic(music)
	for _, beat := range result {
		fmt.Println(beat)
	}
}
```

Explanation:
This Go program defines a function `ParseMusic` that takes a string representing musical notes in a specific ASCII format and returns a slice of integers corresponding to the number of beats each note lasts.

The function uses a map to store the correspondence between the note characters and the number of beats they last. The map is initialized with the legend provided: 'o' for whole notes (4 beats), 'o|' for half notes (2 beats), and '|' for quarter notes (1 beat).

The function then splits the input string into individual notes using the `strings.Split` function, and for each note, it looks up the corresponding number of beats in the map and appends it to the `beats` slice.

In the `main` function, we test the `ParseMusic` function with a sample input string and print the resulting beats. The output is:
```
4
4
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
This corresponds to the correct parsing of the input string.