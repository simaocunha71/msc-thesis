You can use the len function in Go to get the length of a string. Here's the corrected code:

```go
func Strlen(str string) int {
    return len(str)
}
```

This code returns the length of the given string `str`. If `str` is an empty string, the length will be 0. If `str` is 'abc', the length will be 3.