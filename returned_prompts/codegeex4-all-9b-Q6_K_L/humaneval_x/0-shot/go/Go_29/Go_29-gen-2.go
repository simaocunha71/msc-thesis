Here is a solution in Go:

```go
func FilterByPrefix(strings []string, prefix string) []string {
    var result []string
    for _, s := range strings {
        if strings.HasPrefix(s, prefix) {
            result = append(result, s)
        }
    }
    return result
}
```

This function iterates over the input list of strings and checks if each string starts with the given prefix using the `strings.HasPrefix` function. If it does, the string is appended to the `result` slice. Finally, the `result` slice is returned.