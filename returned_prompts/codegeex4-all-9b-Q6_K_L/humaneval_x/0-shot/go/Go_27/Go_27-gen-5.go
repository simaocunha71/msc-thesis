```go
func FlipCase(str string) string {
    builder := strings.Builder{}
    for _, c := range str {
        if 'a' <= c && c <= 'z' {
            builder.WriteRune(c - 'a' + 'A')
        } else if 'A' <= c && c <= 'Z' {
            builder.WriteRune(c - 'A' + 'a')
        } else {
            builder.WriteRune(c)
        }
    }
    return builder.String()
}
```
