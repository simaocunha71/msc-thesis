To solve this problem in Go, you can use a map to keep track of the characters that have been seen. The map's keys will be the distinct characters, and the values can be anything (in this case, we can use the boolean value `true` as a placeholder). We iterate over the string, convert each character to lowercase, and check if it's already in the map. If not, we increment the count and add the character to the map.

Here's how you can implement the `CountDistinctCharacters` function:

```go
package main

import (
    "fmt"
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
func CountDistinctCharacters(str string) int {
    seen := make(map[rune]bool)
    count := 0

    // Iterate over the string
    for _, char := range strings.ToLower(str) {
        // Convert character to lowercase
        if !seen[char] {
            // If character is not seen, increment count and mark it as seen
            count++
            seen[char] = true
        }
    }

    return count
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
    fmt.Println(CountDistinctCharacters("Jerry"))  // Output: 4
}
```

This function converts the input string to lowercase and then iterates over each character. If a character is not already in the `seen` map, it increments the `count` and adds the character to the map. Finally, it returns the `count` of distinct characters.