```go
func Simplify(x, n string) bool {
    numeratorX, _ := strconv.Atoi(strings.Split(x, "/")[0])
    denominatorX, _ := strconv.Atoi(strings.Split(x, "/")[1])
    numeratorN, _ := strconv.Atoi(strings.Split(n, "/")[0])
    denominatorN, _ := strconv.Atoi(strings.Split(n, "/")[1])

    if numeratorX * denominatorN == numeratorN * denominatorX {
        return true
    }

    return false
}
```