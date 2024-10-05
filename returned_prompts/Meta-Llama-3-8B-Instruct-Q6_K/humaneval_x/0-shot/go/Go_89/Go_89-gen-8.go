Here is a possible implementation of the `Encrypt` function in Go:
```go
func Encrypt(s string) string {
    result := ""
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            // Calculate