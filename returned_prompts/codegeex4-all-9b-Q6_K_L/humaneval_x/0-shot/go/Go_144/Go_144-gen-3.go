```go
func Simplify(x, n string) bool {
    a, _ := strconv.Atoi(strings.Split(x, "/")[0])
    b, _ := strconv.Atoi(strings.Split(x, "/")[1])
    c, _ := strconv.Atoi(strings.Split(n, "/")[0])
    d, _ := strconv.Atoi(strings.Split(n, "/")[1])
    
    return a*c % b*d == 0
}
```
