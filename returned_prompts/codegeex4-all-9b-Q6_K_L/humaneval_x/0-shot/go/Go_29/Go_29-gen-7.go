Here is a solution to the problem:

```go
func FilterByPrefix(strings []string, prefix string) []string {
    result := make([]string, 0)
    for _, s := range strings {
        if strings.HasPrefix(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}
```

This function takes in a list of strings and a prefix as parameters. It creates a new empty list called `result`. It then iterates over the input list of strings. For each string in the list, it checks if the string starts with the given prefix using the `strings.HasPrefix()` function. If the string starts with the prefix, it appends the string to the `result` list. Finally, it returns the `result` list, which contains only the strings that start with the given prefix.