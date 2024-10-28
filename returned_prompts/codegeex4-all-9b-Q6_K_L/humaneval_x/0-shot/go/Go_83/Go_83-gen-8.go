```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 2
    }
    return 2 * int(math.Pow(9, float64(n-2)))
}
```