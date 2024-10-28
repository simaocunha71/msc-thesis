To count the distinct characters in a given string, we can use a map to keep track of the characters we've seen. Here's the updated function:

```go
func CountDistinctCharacters(str string) int {
    // Convert the string to lowercase to ignore case
    str = strings.ToLower(str)
    
    // Create a map to store the characters
    distinctChars := make(map[rune]bool)
    
    // Iterate over the string and add each character to the map
    for _, char := range str {
        distinctChars[char] = true
    }
    
    // The number of distinct characters is the size of the map
    return len(distinctChars)
}
```

This function first converts the string to lowercase using `strings.ToLower(str)`. Then it creates a map called `distinctChars` to store the characters. It then iterates over the string and adds each character to the map. Finally, it returns the size of the map, which is the number of distinct characters in the string.