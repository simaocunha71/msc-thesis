```go
func Simplify(x, n string) bool {
    var a, b, c, d int
    fmt.Sscanf(x, "%d/%d", &a, &b)
    fmt.Sscanf(n, "%d/%d", &c, &d)
    return a*d == b*c
}
```
