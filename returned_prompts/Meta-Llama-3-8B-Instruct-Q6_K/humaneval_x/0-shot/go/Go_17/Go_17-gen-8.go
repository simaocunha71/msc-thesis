```go
package main

import (
    "fmt"
    "strings"
)

func ParseMusic(music_string string) []int {
    notes := strings.Split(music_string, " ")
    result := make([]int, 0, len(notes))
    for _, note := range notes {
        switch note {
        case "o":
            result = append(result, 4)
        case "o|":
            result = append(result, 2)
        case ".|":
            result = append(result, 1)
        default:
            fmt.Println("Unknown note:", note)
        }
    }
    return result
}

func main() {
    fmt.Println(ParseMusic("o o| .| o| o| .| .| .| .| o o"))
}
```

Output:
```
[4 2 1 2 2 1 1 1 1 4 4]
```
This function splits the input string into individual notes, then uses a switch statement to determine how many beats each note lasts. It returns a slice of integers representing the number of beats each note lasts. The function handles unknown notes by printing a message to the console. In the main function, we test the function with the provided example input. The output is a slice of integers corresponding to the number of beats each note lasts.