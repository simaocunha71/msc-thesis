Here is a solution in Go:

```go
package main

import (
	"fmt"
	"strings"
)

func ParseMusic(music_string string) []int {
	notes := strings.Split(music_string, " ")
	beats := make([]int, 0)
	for _, note := range notes {
		switch note {
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

In this code, we first split the input string into individual notes. Then, we iterate over each note and switch on its value. If the note is "o", we append 4 to the beats slice. If the note is "o|", we append 2 to the beats slice. If the note is ".|", we append 1 to the beats slice. Finally, we return the beats slice.

When you run this code, it should output `[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]`, which is the correct output for the input string "o o| .| o| o| .| .| .| .| o o".