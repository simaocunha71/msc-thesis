```go
func FlipCase(str string) string {
    result := make([]rune, len(str))
    for i, c := range str {
        if unicode.IsUpper(c) {
            result[i] = unicode.ToLower(c)
        } else {
            result[i] = unicode.ToUpper(c)
        }
    }
    return string(result)
}
```
