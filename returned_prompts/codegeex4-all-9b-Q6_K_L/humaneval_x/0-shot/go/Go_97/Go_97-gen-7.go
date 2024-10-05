```go
func Multiply(a, b int) int {
    return math.Abs(int(math.Mod(float64(a), 10)) * int(math.Mod(float64(b), 10)))
}
```