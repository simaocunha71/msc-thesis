```go
func IsSimplePower(x int,n int) bool {
    for i := 0; i <= 100; i++ {
        if int(math.Pow(float64(n), float64(i))) == x {
            return true
        }
    }
    return false
}
```
