```go
func FlipCase(str string) string {
    return strings.Map(func(r rune) rune {
        if r >= 'A' && r <= 'Z' {
            return r + ('a' - 'A')
        } else if r >= 'a' && r <= 'z' {
            return r - ('a' - 'A')
        }
        return r
    }, str)
}
```
