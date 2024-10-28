Here's the solution for your problem:

```go
func Concatenate(strings []string) string {
    result := ""
    for _, str := range strings {
        result += str
    }
    return result
}
```

This function takes a slice of strings as an argument and concatenates them into a single string. It uses a for loop to iterate over each string in the slice and appends it to the result string. Finally, it returns the concatenated string.