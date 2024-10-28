Here is a solution in Go:

```go
func AllPrefixes(str string) []string {
    prefixes := make([]string, len(str))
    for i := range str {
        prefixes[i] = str[:i+1]
    }
    return prefixes
}
```

This function takes a string as input and returns a slice of strings. The slice is initialized with a length equal to the length of the input string. The for loop iterates over the range of the input string and assigns each prefix of the input string to the corresponding element in the slice. The prefix is generated using string slicing with the `[:i+1]` syntax, which takes a substring from the start of the string up to and including the ith character. Finally, the function returns the slice of prefixes.