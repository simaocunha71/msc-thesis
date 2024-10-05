```go
func IsSimplePower(x int,n int) bool {
    if n == 1 {
        return x == 1
    }
    if x < n {
        return false
    }
    if x%n != 0 {
        return false
    }
    return IsSimplePower(x/n, n)
}
```
