```go
func IsSimplePower(x int,n int) bool {
    if x == 1 {
        return true
    }
    if x % n != 0 {
        return false
    }
    return IsSimplePower(x/n, n)
}
```
