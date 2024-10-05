package main

import (
	"fmt"
	"strings"
)

func ParseMusic(music_string string) []int {
	var parsed []int
	for _, v := range strings.Split(music_string, " ") {
		switch v {
		case "o":
			parsed = append(parsed, 4)
		case "o|":
			parsed = append(parsed, 2)
		case ".|":
			parsed = append(parsed, 1)
		}
	}
	return parsed
}

func main() {
	fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
