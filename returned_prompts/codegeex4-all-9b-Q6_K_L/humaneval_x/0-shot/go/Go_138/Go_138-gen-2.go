```go
func IsEqualToSumEven(n int) bool {
    if n%2 != 0 {
        return false
    }
    for i := 2; i <= n; i += 2 {
        if n-i == 0 {
            return true
        }
    }
    return false
}
```