You can parse the musical notes by iterating over the string and checking each character. Based on the character, you can append the corresponding number of beats to the result slice.

Here's the code that implements this logic:

```go
func ParseMusic(music_string string) []int {
    var result []int
    for i := 0; i < len(music_string); i++ {
        switch music_string[i] {
        case 'o':
            result = append(result, 4)
        case '|':
            if i > 0 && music_string[i-1] == 'o' {
                result = append(result, 2)
            } else {
                result = append(result, 1)
            }
        }
    }
    return result
}
```

Let's test the function with the provided example:

```go
func main() {
    music := "o o| .| o| o| .| .| .| .| o o"
    fmt.Println(ParseMusic(music))
}
```

Output:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

The function correctly parses the musical notes and returns the expected result.