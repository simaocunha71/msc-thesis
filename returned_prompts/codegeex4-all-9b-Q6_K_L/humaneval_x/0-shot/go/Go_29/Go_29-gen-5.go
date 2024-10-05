You can solve this using a simple for loop and the built-in strings.HasPrefix function. Here is a simple implementation:

```go
func FilterByPrefix(strings []string, prefix string) []string {
    result := []string{}
    for _, str := range strings {
        if strings.HasPrefix(str, prefix) {
            result = append(result, str)
        }
    }
    return result
}
```

This function iterates over the input slice of strings, and for each string it checks if it starts with the given prefix using the strings.HasPrefix function. If it does, it adds the string to the result slice. Finally, it returns the result slice.