You can use the `filter` function from the `strings` package. Here's how you can do it:

```go
func FilterByPrefix(strings []string, prefix string) []string {
    return filter(strings, func(s string) bool {
        return strings.HasPrefix(s, prefix)
    })
}
```

This function uses the `strings.HasPrefix` function to check if a string starts with the given prefix. It then filters out any strings that don't match this condition.