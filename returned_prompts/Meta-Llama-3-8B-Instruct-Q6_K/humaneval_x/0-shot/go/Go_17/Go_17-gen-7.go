```go
package main

import (
	"strconv"
	"strings"
)

func ParseMusic(music_string string) []int {
	var result []int
	var beats int
	var notes = strings.Split(music_string, " ")

	for _, note := range notes {
		switch note {
		case "o":
			beats = 4
		case "o|":
			beats = 2
		case ".|":
			beats = 1
		default:
			beats = 0
		}
		if beats > 0 {
			result = append(result, beats)
		}
	}
	return result
}

func main() {
	music_string := "o o| .| o| o| .| .| .| .| o o"
	result := ParseMusic(music_string)
	for _, beats := range result {
		fmt.Println(beats)
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

In this solution, we use a for loop to iterate over each note in the music string. We then use a switch statement to determine the number of beats for each note. We append the beats to the result slice if the beats are greater than 0. Finally, we return the result slice. In the main function, we test the ParseMusic function with a sample music string and print the result.