```go
func Longest(strings []string) interface{}{
    if len(strings) == 0 {
        return nil
    }

    var longest string
    for _, s := range strings {
        if len(s) > len(longest) {
            longest = s
        }
    }

    return longest
}
```