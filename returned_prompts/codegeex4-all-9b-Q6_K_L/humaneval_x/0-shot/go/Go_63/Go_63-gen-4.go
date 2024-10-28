```go
func Fibfib(n int) int {
    if n < 3 {
        return n - 1
    }
    return Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3)
}
```