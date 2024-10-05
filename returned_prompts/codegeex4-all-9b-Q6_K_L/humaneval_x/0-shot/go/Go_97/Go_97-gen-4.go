```go
func Multiply(a, b int) int {
    return abs(a%10) * abs(b%10)
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```