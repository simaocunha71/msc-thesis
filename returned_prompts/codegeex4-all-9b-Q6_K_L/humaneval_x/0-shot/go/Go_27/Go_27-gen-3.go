```go
func FlipCase(str string) string {
    return strings.Map(func(r rune) rune {
        if r >= 'A' && r <= 'Z' {
            return r + 32
        } else if r >= 'a' && r <= 'z' {
            return r - 32
        }
        return r
    }, str)
}
```
