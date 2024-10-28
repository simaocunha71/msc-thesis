```go
func FlipCase(str string) string {
    b := make([]byte, len(str))
    for i, c := range str {
        if c >= 'a' && c <= 'z' {
            b[i] = c - 32
        } else if c >= 'A' && c <= 'Z' {
            b[i] = c + 32
        } else {
            b[i] = c
        }
    }
    return string(b)
}
```
