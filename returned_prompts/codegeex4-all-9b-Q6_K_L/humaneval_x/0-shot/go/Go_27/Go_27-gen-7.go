```go
func FlipCase(str string) string {
    out := make([]byte, len(str))
    for i := 0; i < len(str); i++ {
        if str[i] >= 'a' && str[i] <= 'z' {
            out[i] = str[i] - 32
        } else if str[i] >= 'A' && str[i] <= 'Z' {
            out[i] = str[i] + 32
        } else {
            out[i] = str[i]
        }
    }
    return string(out)
}
```