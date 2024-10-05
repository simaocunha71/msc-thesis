To count the distinct characters in a string, you can use a map to keep track of the characters you've seen. Here's a possible implementation:

```go
func CountDistinctCharacters(str string) int {
    seen := make(map[rune]bool)
    for _, char := range str {
        seen[char] = true
    }
    return len(seen)
}
```

This implementation works by iterating over each character in the string and adding it to the `seen` map. Since map keys must be unique, this effectively filters out duplicate characters. Finally, we return the number of keys in the map, which is the count of distinct characters.