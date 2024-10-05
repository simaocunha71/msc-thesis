```go
func Simplify(x, n string) bool {
    a, b := strings.Split(x, "/")
    c, d := strings.Split(n, "/")
    x, _ := strconv.Atoi(a)
    y, _ := strconv.Atoi(b)
    z, _ := strconv.Atoi(c)
    w, _ := strconv.Atoi(d)
    return (x*z)%y*w == 0
}
```
