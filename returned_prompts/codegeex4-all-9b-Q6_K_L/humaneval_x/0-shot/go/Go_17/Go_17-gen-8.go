Here is a simple solution in Go:

```go
func ParseMusic(music_string string) []int {
    music := strings.Split(music_string, " ")
    result := make([]int, 0, len(music))

    for _, note := range music {
        switch note {
        case "o":
            result = append(result, 4)
        case "o|":
            result = append(result, 2)
        case ".|":
            result = append(result, 1)
        }
    }

    return result
}
```
This function first splits the input string into an array of notes, then iterates through the array and for each note, it appends the corresponding number of beats to the result array. This code assumes that the input string is always in the correct format and does not perform any error checking.