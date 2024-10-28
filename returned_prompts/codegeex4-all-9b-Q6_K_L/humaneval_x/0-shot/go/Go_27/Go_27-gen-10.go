```go
func FlipCase(s string) string {
    runes := []rune(s)
    for i, r := range runes {
        if unicode.IsUpper(r) {
            runes[i] = unicode.ToLower(r)
        } else if unicode.IsLower(r) {
            runes[i] = unicode.ToUpper(r)
        }
    }
    return string(runes)
}
```