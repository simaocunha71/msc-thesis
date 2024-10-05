```go
func Multiply(a, b int) int {
    return int(math.Abs(float64(a%10 * b%10)))
}
```