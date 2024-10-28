You can use a for loop and the built-in string slicing to generate the prefixes. Here's how you can do it:

```go
func AllPrefixes(str string) []string {
    prefixes := make([]string, len(str))
    for i := range str {
        prefixes[i] = str[:i+1]
    }
    return prefixes
}
```

This function creates a slice of strings with the same length as the input string. It then populates the slice by iterating over the input string and using string slicing to get the prefix up to the current index.

Please note that the first element of the slice will be an empty string, as it represents the prefix of an empty string. If you want to exclude the empty string from the result, you can simply return prefixes[1:] instead of prefixes.