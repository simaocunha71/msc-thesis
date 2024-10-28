```go
func Simplify(x, n string) bool {
    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_den, _ := strconv.Atoi(strings.Split(x, "/")[1])
    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_den, _ := strconv.Atoi(strings.Split(n, "/")[1])

    return (x_num * n_den) % (x_den * n_num) == 0
}
```