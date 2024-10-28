```go
func StartsOneEnds(n int) int {
    if n < 1 {
        return 0
    }
    if n == 1 {
        return 2
    }
    return 18 * int(math.Pow10(n-2))
}
```