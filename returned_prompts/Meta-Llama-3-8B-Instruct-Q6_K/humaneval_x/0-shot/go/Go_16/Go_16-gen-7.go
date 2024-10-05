```go
package main

import (
    "strings"
    "fmt"
)

func CountDistinctCharacters(str string) int {
    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, char := range str {
        if _, ok := charSet[char]; !ok {
            charSet[char] = true
        }
    }
    return len(charSet)
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ")) // Output: 3
    fmt.Println(CountDistinctCharacters("Jerry")) // Output: 4
}
```


Explanation:
1. First, we convert the input string to lowercase using `strings.ToLower` to ensure the comparison is case-insensitive.
2. We create a map of runes (which are the actual characters in the string) to booleans. This map will store the distinct characters in the string.
3. We iterate over the characters in the string using a range loop. For each character, we check if it's already present in the map using the `ok` variable. If it's not present, we add it to the map.
4. Finally, we return the length of the map, which represents the number of distinct characters in the string.

The `main` function demonstrates the usage of the `CountDistinctCharacters` function with two test cases. The output shows that the function correctly counts the distinct characters in each string.