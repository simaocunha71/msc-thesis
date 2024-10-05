You can use the built-in len() function in Go to get the length of a string. Here's the corrected version of your function:

```go
func Strlen(str string) int {
    return len(str)
}
```

This function takes a string as an argument and returns its length as an integer. For example, calling Strlen("abc") will return 3.