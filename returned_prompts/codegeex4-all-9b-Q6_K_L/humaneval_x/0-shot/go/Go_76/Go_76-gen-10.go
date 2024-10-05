```go
func IsSimplePower(x int, n int) bool {
    if n == 0 {
        return x == 1
    }
    power := 1
    for power <= x {
        if power == x {
            return true
        }
        power *= n
    }
    return false
}
```
