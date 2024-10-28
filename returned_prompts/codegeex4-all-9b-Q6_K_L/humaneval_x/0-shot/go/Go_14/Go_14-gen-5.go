You can create a simple function that loops through the string and appends each character to the result slice. Here's how you can do it:

```go
func AllPrefixes(str string) []string {
    result := make([]string, 0, len(str))
    for i := 1; i <= len(str); i++ {
        result = append(result, str[:i])
    }
    return result
}
```

This function starts by creating an empty slice with a length equal to the length of the input string. Then, it loops through the string from 1 to the length of the string, appending each prefix to the slice. Finally, it returns the slice of prefixes.