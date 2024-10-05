Here is the Go code to solve the problem:

```go
func ParseMusic(music_string string) []int {
    var result []int
    for _, note := range music_string {
        switch note {
        case 'o':
            result = append(result, 4)
        case 'o|':
            result = append(result, 2)
        case '.|':
            result = append(result, 1)
        }
    }
    return result
}
```

The code iterates over each character in the input string and checks if it is one of the notes 'o', 'o|', or '.|'. If it is, the corresponding number of beats is appended to the result slice. Finally, the result slice is returned.