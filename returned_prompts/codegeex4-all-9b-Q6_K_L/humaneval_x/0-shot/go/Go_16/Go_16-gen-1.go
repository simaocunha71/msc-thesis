Here is a solution in Go:

```go
func CountDistinctCharacters(str string) int {
    distinctCharacters := make(map[string]bool)
    for _, char := range strings.ToLower(str) {
        distinctCharacters[string(char)] = true
    }
    return len(distinctCharacters)
}
```

This code works by creating a map of boolean values and iterating over the string. The `strings.ToLower` function is used to ensure that the case of the characters is ignored. For each character, it adds it to the map with the value `true`. Since maps in Go cannot have duplicate keys, this automatically removes any duplicate characters. Finally, it returns the length of the map, which is the number of distinct characters in the string.