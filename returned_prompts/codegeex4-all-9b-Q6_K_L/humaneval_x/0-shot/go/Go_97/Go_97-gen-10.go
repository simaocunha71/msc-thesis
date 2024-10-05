```go
func Multiply(a, b int) int {
    return abs(a%10) * abs(b%10)
}

func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}
```