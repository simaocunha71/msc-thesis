Here is a simple implementation using Go's built-in `strings` package:

```go
package main

import (
    "strings"
)

// Given a string, find out how many distinct characters (regardless of case) does it consist of
// >>> CountDistinctCharacters('xyzXYZ')
// 3
// >>> CountDistinctCharacters('Jerry')
// 4
func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str) // Convert the string to lowercase
    charSet := make(map[rune]bool) // Create a map to store distinct characters
    for _, char := range str {
        if _, ok := charSet[char]; !ok {
            charSet[char] = true // Add the character to the map if it's not already present
        }
    }
    return len(charSet) // Return the number of distinct characters
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
    fmt.Println(CountDistinctCharacters("Jerry")) // Output: 4
}
```
The code first converts the string to lowercase to ensure that the same character in different cases is not treated as distinct. Then it creates a map to store the distinct characters. It iterates over the string, and for each character, it checks if it's already present in the map. If not, it adds it to the map. Finally, it returns the number of distinct characters by getting the length of the map.