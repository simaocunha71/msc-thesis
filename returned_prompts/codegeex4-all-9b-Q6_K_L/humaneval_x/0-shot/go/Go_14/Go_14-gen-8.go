Here's a solution in Go:

```go
func AllPrefixes(str string) []string {
    prefixes := make([]string, len(str))
    for i := range str {
        prefixes[i] = str[:i+1]
    }
    return prefixes
}
```

This function creates an empty slice of strings with the same length as the input string. Then it uses a loop to iterate through each character in the input string and appends the prefix (from the start of the string up to and including the current character) to the slice. Finally, it returns the slice of prefixes.