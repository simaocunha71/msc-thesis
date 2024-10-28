
Here's a way to do it:

```go
package main

import (
    "fmt"
    "strings"
)

func ParseMusic(music_string string) []int {
    beats := make([]int, 0)
    for _, c := range music_string {
        switch c {
        case 'o':
            beats = append(beats, 4)
        case 'o|':
            beats = append(beats, 2)
        case '.':
            beats = append(beats, 1)
        }
    }
    return beats
}

func main() {
    music := "o o| .| o| o| o o"
    fmt.Println(ParseMusic(music))
}
```

This program defines a function `ParseMusic` that takes a musical note string and returns a list of integers. The function iterates over the characters in the string. If the character is `'o'`, the function appends `4` to the list of beats. If the character is `'o|'`, the function appends `2` to the list of beats. If the character is `'.'`, the function appends `1` to the list of beats.

The `main` function demonstrates the usage of the `ParseMusic` function by passing a musical note string and printing the returned list of beats.

Note: This solution uses the `strings` package to iterate over the characters in the string.

Here are some additional notes about the solution:

- The `ParseMusic` function takes a single argument, `music_string`, of type `string`.
- The `for`, `range` statement iterates over the characters in the `music_string`.
- The `switch` statement is used to determine the number of beats for each note.
- The `case` statements check the value of the character `c`.
- The `append` function is used to add the number of beats to the `beats` slice.
- The `return` statement is used to return the `beats` slice.
- The `main` function demonstrates the usage of the `ParseMusic` function by passing a musical note string and printing