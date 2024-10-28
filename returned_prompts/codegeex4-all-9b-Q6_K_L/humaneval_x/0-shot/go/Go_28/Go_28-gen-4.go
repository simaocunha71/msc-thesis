You can use strings.Join to concatenate a slice of strings into a single string. Here is how you can do it:

```go
func Concatenate(strings []string) string {
    return strings.Join(strings, "")
}
```

This function takes a slice of strings as an argument and returns a single string that is the concatenation of all the strings in the slice. The second argument to strings.Join is the separator to be used between the strings. In this case, we use an empty string as the separator, so there is no space between the strings in the resulting string.