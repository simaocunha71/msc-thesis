To count the distinct characters in a string, you can convert the string to a slice of runes, which allows you to handle Unicode characters properly. Then, you can use a map to track the unique characters. Here's the complete solution:

```go
import (
    "strings"
)

func CountDistinctCharacters(str string) int {
    // Convert the string to a slice of runes
    runes := []rune(str)
    
    // Create a map to track unique characters
    seen := make(map[rune]bool)
    
    // Iterate over the runes and mark them as seen
    for _, r := range runes {
        seen[r] = true
    }
    
    // The number of unique characters is the size of the map
    return len(seen)
}
```

This function works by iterating over each rune in the string and adding it to the `seen` map. Since maps in Go cannot have duplicate keys, this effectively counts the unique characters. The length of the `seen` map gives the number of distinct characters in the string.