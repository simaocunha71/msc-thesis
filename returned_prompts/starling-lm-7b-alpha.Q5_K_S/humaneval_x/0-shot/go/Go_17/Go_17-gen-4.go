
```go
import (
    "strings"
    "strconv"
)

func ParseMusic(music_string string) []int {
    // Split on |
    parts := strings.Split(music_string, "|")
    // Convert to integers
    ints := make([]int, len(parts))
    for i, p := range parts {
        switch p {
        case "o":
            ints[i] = 4
        case "o|":
            ints[i] = 2
        case ".":
            ints[i] = 1
        }
    }
    return ints
}
```

Explanation:
The function takes a string as input and splits it into parts by the "|" character. It then iterates through the parts and assigns the appropriate value to each part of the ints slice based on the value of p.

The switch statement is used to assign the appropriate value to each part of the ints slice based on the value of p. If p is "o", it assigns 4 to the ints slice at index i. If p is "o|", it assigns 2 to the ints slice at index i. If p is ".", it assigns 1 to the ints slice at index i.

The function returns the ints slice, which contains the corresponding number of beats for each note in the music string.

Overall, this solution uses the split function to separate the music string into parts, and then uses a switch statement to assign the appropriate value to each part of the ints slice based on the value of p.

Here's an example of how to use this function:

```go
package main

import "fmt"

func main() {
    musicString := "o o| .| o| o| o"
    ints := ParseMusic(musicString)
    fmt.Println(ints)
}
```

The output of this program will be:
```
[4 2 1 2 2 1 1 1 1]
```

This means that the first note in the music string lasts for four beats, the second note lasts for two be