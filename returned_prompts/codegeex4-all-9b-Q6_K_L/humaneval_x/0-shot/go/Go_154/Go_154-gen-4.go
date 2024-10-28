```go
func CycpatternCheck(a, b string) bool {
    if len(a) < len(b) {
        return false
    }
    b += b
    return strings.Contains(b, a)
}
```
