To count the distinct characters in a given string, you can use a map to keep track of the characters you have encountered. Here's how you can implement the function `CountDistinctCharacters` in Go:

```go
import (
    "strings"
)

func CountDistinctCharacters(str string) int {
    // Convert the string to lowercase to count case-insensitively
    str = strings.ToLower(str)
    
    // Create a map to keep track of distinct characters
    distinctChars := make(map[rune]bool)
    
    // Iterate over each character in the string
    for _, char := range str {
        // Add the character to the map
        distinctChars[char] = true
    }
    
    // The number of distinct characters is the number of keys in the map
    return len(distinctChars)
}
```

In this function, we first convert the input string to lowercase using `strings.ToLower(str)` to ensure that we count characters case-insensitively. Then, we create a map `distinctChars` where the keys are the characters from the string, and the values are booleans indicating whether the character has been encountered. We iterate over each character in the string and add it to the map. Finally, we return the number of distinct characters by getting the length of the map with `len(distinctChars)`.