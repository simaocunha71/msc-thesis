```go
func Multiply(a, b int) int {
    return int(math.Mod(float64(a), 10)) * int(math.Mod(float64(b), 10))
}
```